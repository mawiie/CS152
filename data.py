data = [
    {"Name": "Fogón Asado", "Cuisine": "Steakhouse, Argentine", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.8, "NumReviews": 37,  # Fogón Asado: Yelp 4.8 (37 reviews)&#8203;:contentReference[oaicite:0]{index=0}
     "Distance_km": 4.0, "Price": "$$$$", "WaitTime": "No wait (reservation only)", "EnglishFriendly": True},
    {"Name": "Don Julio", "Cuisine": "Argentine", "Dietary": "Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.4, "NumReviews": 527,  # Don Julio: Yelp 4.4 (527 reviews)&#8203;:contentReference[oaicite:1]{index=1}
     "Distance_km": 4.2, "Price": "$$$", "WaitTime": "60+ min without reservation", "EnglishFriendly": True},
    {"Name": "La Cabrera", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 3.8, "NumReviews": 326,  # La Cabrera: Yelp 3.8 (326 reviews)&#8203;:contentReference[oaicite:2]{index=2}
     "Distance_km": 4.0, "Price": "$$$", "WaitTime": "30-60 min at peak hours", "EnglishFriendly": True},
    {"Name": "Parrilla Peña", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 100,
     "Distance_km": 1.5, "Price": "$$", "WaitTime": "Short wait at lunch rush", "EnglishFriendly": False},
    {"Name": "La Carnicería", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.6, "NumReviews": 280,  # La Carnicería: ~280 Yelp reviews&#8203;:contentReference[oaicite:3]{index=3}
     "Distance_km": 4.0, "Price": "$$$", "WaitTime": "No reservations, ~30 min wait", "EnglishFriendly": True},
    {"Name": "Mishiguene", "Cuisine": "Middle-Eastern", 
     "Dietary": "Vegetarian Friendly, Vegan Options, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.2, "NumReviews": 76,  # Mishiguene: special diets&#8203;:contentReference[oaicite:4]{index=4}; Yelp 4.2 (76 reviews)&#8203;:contentReference[oaicite:5]{index=5}
     "Distance_km": 3.5, "Price": "$$$", "WaitTime": "Reservation recommended", "EnglishFriendly": True},
    {"Name": "El Preferido de Palermo", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.3, "NumReviews": 150,
     "Distance_km": 4.0, "Price": "$$$", "WaitTime": "Up to 30 min at peak times", "EnglishFriendly": True},
    {"Name": "Chori", "Cuisine": "Argentine-(StreetFood)", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 200,
     "Distance_km": 4.1, "Price": "$", "WaitTime": "Short queue at lunch", "EnglishFriendly": True},
    {"Name": "Santos Manjares", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.7, "NumReviews": 100,
     "Distance_km": 1.0, "Price": "$$", "WaitTime": "No wait usually", "EnglishFriendly": True},
    {"Name": "Siga La Vaca", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 3.8, "NumReviews": 63,
     "Distance_km": 2.0, "Price": "$$$", "WaitTime": "No wait (large capacity)", "EnglishFriendly": True},
    {"Name": "Florería Atlántico", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 300,
     "Distance_km": 2.5, "Price": "$$$$", "WaitTime": "No wait (evenings only)", "EnglishFriendly": True},
    {"Name": "Elena", "Cuisine": "International", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.7, "NumReviews": 77,
     "Distance_km": 2.0, "Price": "$$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Aramburu", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.8, "NumReviews": 29,
     "Distance_km": 1.8, "Price": "$$$$", "WaitTime": "No wait (reservation only)", "EnglishFriendly": True},
    {"Name": "Chila", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.6, "NumReviews": 50,
     "Distance_km": 2.5, "Price": "$$$$", "WaitTime": "No wait (reservation only)", "EnglishFriendly": True},
    {"Name": "Osaka (Palermo)", "Cuisine": "Japanese/Peruvian", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 76,
     "Distance_km": 4.0, "Price": "$$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Sarkis", "Cuisine": "Middle Eastern (Armenian)", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash only", "Rating": 4.4, "NumReviews": 2688,  # Sarkis: cash only (no credit cards)&#8203;:contentReference[oaicite:6]{index=6}
     "Distance_km": 5.0, "Price": "$$", "WaitTime": "~30 min wait (no reservations)", "EnglishFriendly": False},
    {"Name": "Pizzería Güerrín", "Cuisine": "Italian", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 547,
     "Distance_km": 0.5, "Price": "$", "WaitTime": "No wait (large venue)", "EnglishFriendly": False},
    {"Name": "El Cuartito", "Cuisine": "Italian", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.0, "NumReviews": 374,
     "Distance_km": 1.0, "Price": "$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "La Brigada", "Cuisine": "Argentine", "Dietary": "Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.0, "NumReviews": 200,
     "Distance_km": 2.2, "Price": "$$$", "WaitTime": "Short wait at peak", "EnglishFriendly": True},
    {"Name": "Cabaña Las Lilas", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.0, "NumReviews": 532,
     "Distance_km": 2.8, "Price": "$$$$", "WaitTime": "No wait (large venue)", "EnglishFriendly": True},
    {"Name": "El Pobre Luis", "Cuisine": "Uruguayan", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 50,
     "Distance_km": 8.0, "Price": "$$$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "Gran Parrilla del Plata", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.3, "NumReviews": 117,
     "Distance_km": 1.8, "Price": "$$$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "Café San Juan (La Cantina)", "Cuisine": "Argentine/Spanish", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.2, "NumReviews": 909,
     "Distance_km": 2.0, "Price": "$$$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "1810 Cocina Regional", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.0, "NumReviews": 10,
     "Distance_km": 5.0, "Price": "$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "La Cocina", "Cuisine": "Argentine (Empanadas)", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 296,
     "Distance_km": 2.5, "Price": "$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "El Sanjuanino", "Cuisine": "Argentine (Empanadas, Locro)", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.0, "NumReviews": 65,
     "Distance_km": 2.2, "Price": "$$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "Perón Perón Restó Bar", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.2, "NumReviews": 100,
     "Distance_km": 5.0, "Price": "$$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "La Mar Cebichería", "Cuisine": "Peruvian", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 100,
     "Distance_km": 5.0, "Price": "$$$", "WaitTime": "No wait (spacious)", "EnglishFriendly": True},
    {"Name": "Sucre", "Cuisine": "Argentine", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 33,
     "Distance_km": 7.0, "Price": "$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Casa Cavia", "Cuisine": "International", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 27,
     "Distance_km": 4.0, "Price": "$$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Don Carlos (La Boca)", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash only", "Rating": 4.0, "NumReviews": 208,  # Don Carlos: only takes cash&#8203;:contentReference[oaicite:7]{index=7}
     "Distance_km": 4.2, "Price": "$$$", "WaitTime": "No wait (small venue)", "EnglishFriendly": False},
    {"Name": "El Obrero", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash only", "Rating": 4.3, "NumReviews": 1275,  # El Obrero: cash only&#8203;:contentReference[oaicite:8]{index=8}
     "Distance_km": 4.5, "Price": "$$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "Oviedo", "Cuisine": "Spanish", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.7, "NumReviews": 1218,
     "Distance_km": 2.5, "Price": "$$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "La Bourgogne", "Cuisine": "French", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 100,
     "Distance_km": 2.2, "Price": "$$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Sottovoce", "Cuisine": "Italian", "Dietary": "Vegetarian Friendly, Vegan Options",
     "Payment": "Cash, Card", "Rating": 4.6, "NumReviews": 100,
     "Distance_km": 2.0, "Price": "$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Fervor", "Cuisine": "Argentine", "Dietary": "Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.1, "NumReviews": 134,
     "Distance_km": 2.0, "Price": "$$$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "Crizia", "Cuisine": "Seafood", "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 37,
     "Distance_km": 4.8, "Price": "$$$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "Xi Bei Feng", "Cuisine": "Chinese", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 5.0, "NumReviews": 5,
     "Distance_km": 4.5, "Price": "$$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "Tandoor", "Cuisine": "Indian", "Dietary": "Vegetarian Friendly, Vegan Options",
     "Payment": "Cash, Card", "Rating": 3.9, "NumReviews": 46,
     "Distance_km": 3.0, "Price": "$$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "Buenos Aires Verde", "Cuisine": "Vegan", "Dietary": "Vegetarian, Vegan, Gluten-free",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 53,
     "Distance_km": 4.0, "Price": "$$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "Café Tortoni", "Cuisine": "Cafe", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.3, "NumReviews": 11000,
     "Distance_km": 0.5, "Price": "$", "WaitTime": "10-20 min line at peak", "EnglishFriendly": False},
    {"Name": "Gran Dabbang", "Cuisine": "South-East Asian", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 327,
     "Distance_km": 3.8, "Price": "$$$", "WaitTime": "~30 min wait (no reservations)", "EnglishFriendly": True},
    {"Name": "Hierro Palermo Parrilla", "Cuisine": "Argentine", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.9, "NumReviews": 1477,
     "Distance_km": 5.0, "Price": "$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Il Matterello (La Boca)", "Cuisine": "Italian", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.5, "NumReviews": 44,
     "Distance_km": 4.3, "Price": "$$", "WaitTime": "No wait", "EnglishFriendly": False},
    {"Name": "La Pécora Nera", "Cuisine": "Italian", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash, Card", "Rating": 4.6, "NumReviews": 44,
     "Distance_km": 2.0, "Price": "$$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True},
    {"Name": "Puerto Cristal", "Cuisine": "International (Seafood)", "Dietary": "Vegetarian Friendly, Vegan Options",
     "Payment": "Cash, Card", "Rating": 4.0, "NumReviews": 2026,
     "Distance_km": 2.0, "Price": "$$$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "Happening (Puerto Madero)", "Cuisine": "International (steak)", "Dietary": "Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 4.1, "NumReviews": 1430,
     "Distance_km": 1.5, "Price": "$$$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "The Argentine Experience", "Cuisine": "Argentine Gourmet", 
     "Dietary": "Vegetarian Friendly, Gluten-free Options",
     "Payment": "Cash, Card", "Rating": 5.0, "NumReviews": 2946,  
     "Distance_km": 5.5, "Price": "$$$$", "WaitTime": "No wait (pre-booked seating)", "EnglishFriendly": True},
    {"Name": "Burger Joint", "Cuisine": "American (fast food)", "Dietary": "Vegetarian Friendly",
     "Payment": "Cash only", "Rating": 4.0, "NumReviews": 1859,
     "Distance_km": 4.5, "Price": "$", "WaitTime": "No wait", "EnglishFriendly": True},
    {"Name": "Niño Gordo", "Cuisine": "Asian BBQ", "Dietary": "None",
     "Payment": "Cash, Card", "Rating": 4.1, "NumReviews": 842, 
     "Distance_km": 4.0, "Price": "$$$", "WaitTime": "No wait (reservations available)", "EnglishFriendly": True}
]
