# crops.py
crops_data = {
    "Cassava": {
        "title": "Cassava (Manihot esculenta)",
        "other_names": "Muhogo, Manioc, Tapioca",
        "overview": "Cassava is the second most important staple crop in Uganda, providing a vital source of food security and income for millions of smallholder farmers due to its resilience to drought and poor soil conditions. Beyond being a staple food, it is also a significant cash crop and has growing industrial uses, with potential for further agro-industrial development. However, the sector is challenged by pests and devastating diseases, particularly Cassava Mosaic Disease and Cassava Brown Streak Disease.",
        "image_url": "/static/images/cassa.png",
        "plant_image_url": "/static/images/cassava.png",
        "varieties": [
            {"type": "Improved Resistant", "name": "NAROCASS 1 & 2", "yield": "35–50 tons/ha", "features": "CBSD & CMD resistant", "use": "Starch, flour, fresh"},
            {"type": "High Yield", "name": "NASE 14", "yield": "40+ tons/ha", "features": "Early maturing, high starch"},
            {"type": "Popular Local", "name": "Bao, TME 14", "yield": "25–35 tons/ha"}
        ],
        "best_planting_time": "• Plant at onset of rains (March–May)\n• Use 10–12 month old healthy stems\n• Spacing: 1m × 1m\n• Plant at 45° angle, 5–6 nodes buried",
        "ideal_conditions": "Temp: 25–32°C | Rainfall: 1000–1500mm | Soil: Sandy loam, pH 5.5–6.5",
        "harvest": "9–18 months after planting",
        "major_pests_diseases": [
            "Major cassava diseases: Cassava Mosaic Disease (CMD) Yellowing and distortion of leaves, stunting of the plant, and reduced root size, Cassava Brown Streak Disease (CBSD) Yellow and green patches (chlorosis) on leaves, brown streaks on upper green stems, and a dry, hard, corky brown rot in the tuberous roots, Cassava Bacterial Blight (CBB) Water-soaked spots on leaves, wilting, defoliation, and die-back of stems, Cassava Anthracnose Cankers (sores) on stems and leaf petiole bases, leading to leaf wilting, defoliation, and shoot die-back.",
            "Pests: Whiteflies (CMD and CBSD viruses), Cassava Mealybug, Cassava Green Mite, Termites, Variegated Grasshopper",
            "Control:  Use of Healthy Planting Materials, Resistant Varieties, Field Sanitation (Roguing), Vector Control, Crop Rotation, Biological Control"
        ],
        "processing_opportunities": [
            "Fresh boiling & pounding",
            "High Quality Cassava Flour (HQCF)",
            "Starch for industry",
            "Animal feed from peels"
        ],
        "sections_order": ["overview", "varieties", "best_planting_time", "ideal_conditions", "harvest", "major_pests_diseases", "processing_opportunities"]
    },
    "Maize": {
        "title": "Maize (Zea mays)",
        "other_names": "Corn, Mahindi",
        "overview": "Maize is Uganda's most important cereal crop and staple food in many regions. Maize is an erect annual grass, typically growing 2 to 3 meters tall. It has a single main stalk (culm) with nodes and broad leaves. It is monoecious, meaning it has separate male flowers (tassel, at the top of the plant) and female flowers (ears, which grow in leaf axils and are covered in husks) on the same plant.",
        "image_url": "/static/images/maiz.png",
        "plant_image_url": "/static/images/maize.png",
        "varieties": [
            {"type": "Hybrid", "name": "Longe 10H, Longe 7H", "yield": "9–12 tons/ha", "features": "Drought tolerant"},
            {"type": "Open Pollinated", "name": "Longe 5", "yield": "7–9 tons/ha"},
            {"type": "Quality Protein", "name": "QPM varieties", "benefit": "Higher nutrition"}
        ],
        "best_planting_time": "• First season: March–May\n• Second season: August–September\n• Spacing: 75cm × 25cm\n• 1–2 seeds per hole",
        "ideal_conditions": "Temp: 24–30°C | Rainfall: 800–1200mm | Soil: Fertile loams, pH 6.0–7.0, other factors are spacing and density, level of fertilizer usage, weed control (first 4-6 weeks after emergence), pests and diseases control (Use an integrated pest management (IPM) approach)",
        "harvest": "90–120 days after planting, dry the harvest thoroughly and store in clean, well-ventilated, and protected area free from mould, insect infestation and rodent damage.",
        "major_pests_diseases": [
            "Pests: Fall Armyworm highly destructive as larvae feed on the leaves , Maize stem borer larvae bore into the maize stem, disrupting nutrient flow, weakening the plant, and creating dead hearts in young plant",
            "Diseases: Maize lethal necrosis disease (MLND) can cause total crop failure as Severe chlorosis (yellowing of leaves), stunted growth, failure to tassel, and rotting cobs, Gray leaf spot (GLS) Appears as oblong, rectangular, tan-to-brown lesions on the leaves, leading to reduced photosynthetic area and shriveled kernels, Maize streak virus (MSV) This viral disease is spread by leafhoppers and causes streaks of yellow and green stripes on the leaves. Severe infection can lead to stunting and reduced yields.",
            "Control measures: Crop Rotation, Field Sanitation, Timely Planting, Weed Management, Proper Fertilization(use of fertilizers), Biopesticides, Seed Treatment, Targeted Insecticides, Resistant Varieties"
        ],
        "processing_opportunities": [
            "Posho (maize flour)",
            "Animal feed",
            "Baby corn export",
            "Brewery (sorghum substitute)"
        ],
        "sections_order": ["overview", "varieties", "best_planting_time", "ideal_conditions", "harvest", "major_pests_diseases", "processing_opportunities"]
    }
}

agri_companies = {
    "Seed Suppliers": [
        {"name": "NARO Uganda", "url": "https://naro.go.ug", "note": "Develops NAROCASS & Longe series"},
        {"name": "FICA Seeds", "url": "https://ficaseeds.com", "note": "Hybrid maize & cassava"},
        {"name": "Victoria Seeds", "url": "https://victoriaseeds.com", "note": "Longe hybrids"},
    ],
    "Buyers & Processors": [
        {"name": "AgroWays (U) Limited", "url": " https://www.agroways.ug/", "note": "An agribusiness company, likely involved in the trade of various agricultural products, including cassava"},
        {"name": "go4WorldBusiness", "url": "https://www.go4worldbusiness.com/suppliers/uganda/cassava.html", "note": "Lists various suppliers and buyers of cassava and related products."},
        {"name": "Arise and Shine Maize Millers Ltd", "url": "https:// ariseandshinemillers.co.ug", "note": "A prominent maize miller and provider of maize flour and bran, with a national network of branches."},
        
    ],
    "Finding Market": [
        {"name": "Freshdi", "url": "https://freshdi.com/buyer-category/Uganda/Cassava", "note": "Lists of active cassava buyers and importers"},
        {"name": "AgroMarketDay", "url": "http://www.agromarketday.com/market/produce/239-looking-for-cassava-buyers ", "note": "A market platform where buyers and sellers can post listings for agricultural produce"},
    ]
}