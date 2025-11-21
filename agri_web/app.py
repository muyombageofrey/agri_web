# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date, timedelta
from crops import crops_data, agri_companies
from meteostat import Point, Daily
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agri.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class FarmLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False, default='My Farm')
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Weather Function (with fallback)
def get_weather_data(lat, lon):
    try:
        point = Point(lat, lon)
        end = date.today()
        start = end - timedelta(days=10)
        data = Daily(point, start, end).fetch()

        if data.empty:
            raise Exception("No weather data")

        current = data.iloc[-1]
        history = data.iloc[-6:-1][::-1].copy()

        history_list = []
        for i, (_, row) in enumerate(history.iterrows()):
            day = end - timedelta(days=5-i)
            history_list.append({
                'day_name': day.strftime('%a'),
                'date': day.strftime('%b %d'),
                'tavg': round(row['tavg'] or 27.0, 1),
                'tmin': round(row['tmin'] or 21.0, 1),
                'tmax': round(row['tmax'] or 32.0, 1),
                'rainfall': round(row['prcp'] or 0.0, 1)
            })

        return {
            'current': {
                'tavg': round(current['tavg'] or 27.5, 1),
                'tmin': round(current['tmin'] or 21.0, 1),
                'tmax': round(current['tmax'] or 32.0, 1),
                'rainfall': round(current['prcp'] or 0.0, 1),
                'condition': 'Sunny' if (current['prcp'] or 0) < 1 else 'Rainy' if (current['prcp'] or 0) > 5 else 'Cloudy',
                'humidity': int(current.get('rhum', 78) or 78)
            },
            'history': history_list
        }
    except Exception as e:
        print("Weather fallback used:", e)
        today = date.today()
        return {
            'current': {
                'tavg': 27.5, 'tmin': 21, 'tmax': 32, 'rainfall': 0.3,
                'condition': 'Partly Cloudy', 'humidity': 78
            },
            'history': [
                {'day_name': (today-timedelta(5)).strftime('%a'), 'date': (today-timedelta(5)).strftime('%b %d'), 'tavg': 26.8, 'tmin': 20, 'tmax': 32, 'rainfall': 1.2},
                {'day_name': (today-timedelta(4)).strftime('%a'), 'date': (today-timedelta(4)).strftime('%b %d'), 'tavg': 27.1, 'tmin': 21, 'tmax': 33, 'rainfall': 0.0},
                {'day_name': (today-timedelta(3)).strftime('%a'), 'date': (today-timedelta(3)).strftime('%b %d'), 'tavg': 27.9, 'tmin': 22, 'tmax': 34, 'rainfall': 0.0},
                {'day_name': (today-timedelta(2)).strftime('%a'), 'date': (today-timedelta(2)).strftime('%b %d'), 'tavg': 26.5, 'tmin': 21, 'tmax': 31, 'rainfall': 8.5},
                {'day_name': (today-timedelta(1)).strftime('%a'), 'date': (today-timedelta(1)).strftime('%b %d'), 'tavg': 27.2, 'tmin': 21, 'tmax': 32, 'rainfall': 0.8},
            ]
        }

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    farm = FarmLocation.query.filter_by(user_id=current_user.id).first()
    if not farm:
        return redirect(url_for('set_location'))

    weather_data = get_weather_data(farm.latitude, farm.longitude)
    news = [
        {"title": "National Agricultural Research Organisation (NARO)", "summary": "Provides news and updates on research, innovation, and technologies in agriculture", "link": "https://news.naro.go.ug/", "published": "2025"},
        {"title": "Daily Monitor (UG) Farming Section", "summary": "Provide daily updates on farming and agribusiness ventures, news, market info, and practical advice.", "link": "https://www.monitor.co.ug/uganda/magazines/farming", "published": "2025"},
        {"title": "Food and Agriculture Organization (FAO) Uganda", "summary": "Provides news on large-scale projects, food security, and climate adaptation initiatives", "link": "https://www.fao.org/uganda/news/en ", "published": "2025"}
    ]

    return render_template('dashboard.html',
                           weather=weather_data['current'],
                           history=weather_data['history'],
                           farm=farm,
                           now=datetime.now(),
                           news=news)

@app.route('/crops')
@login_required
def crops_page():
    return render_template('crops.html', crops=crops_data)

@app.route('/crop/<name>')
@login_required
def crop_detail(name):
    crop = crops_data.get(name.capitalize())
    if not crop:
        flash('Crop not found', 'danger')
        return redirect(url_for('crops_page'))
    return render_template('crop_detail.html', crop=crop, agri_companies=agri_companies)

@app.route('/set_location', methods=['GET', 'POST'])
@login_required
def set_location():
    location = FarmLocation.query.filter_by(user_id=current_user.id).first()
    if request.method == 'POST':
        try:
            lat = float(request.form['lat'])
            lon = float(request.form['lon'])
            name = request.form.get('name', 'My Farm').strip() or 'My Farm'
            if location:
                location.latitude = lat
                location.longitude = lon
                location.name = name
            else:
                location = FarmLocation(user_id=current_user.id, latitude=lat, longitude=lon, name=name)
                db.session.add(location)
            db.session.commit()
            flash('Farm location saved successfully!', 'success')
            return redirect(url_for('dashboard'))
        except:
            flash('Invalid coordinates', 'danger')
    return render_template('set_location.html', location=location)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form['email']).first():
            flash('Email already registered', 'danger')
        else:
            user = User(username=request.form['username'],
                        email=request.form['email'],
                        password=generate_password_hash(request.form['password']))
            db.session.add(user)
            db.session.commit()
            flash('Registered! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/init-db', methods=['GET'])
def init_db():
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(email='farmer@example.com').first():
            demo = User(username='DemoFarmer', email='farmer@example.com',
                        password=generate_password_hash('password123'))
            db.session.add(demo)
            db.session.commit()
        return "Database initialized! Demo user created. You can delete this route now."

if __name__ == '__main__':
  
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(email='farmer@example.com').first():
            demo = User(
                username='DemoFarmer',
                email='farmer@example.com',
                password=generate_password_hash('password123')
            )
            db.session.add(demo)
            db.session.commit()

   
