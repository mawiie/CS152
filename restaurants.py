import pandas as pd
import os
from data import data


def process_payment(payment_str):
    if "Cash only" in payment_str:
        return ["cash"]
    elif "Cash, Card" in payment_str:
        return ["cash", "card"]
    return ["none"]


def process_dietary(dietary_str):
    if dietary_str == "None":
        return []
    options = []
    mappings = {
        "Vegetarian Friendly": "vegetarian",
        "Vegan Options": "vegan",
        "Gluten-free Options": "gluten-free",
        "Vegetarian": "vegetarian",
        "Vegan": "vegan",
        "Gluten-free": "gluten-free"
    }
    for key, value in mappings.items():
        if key in dietary_str:
            options.append(value)
    return options


def process_wait_time(wait_str):
    if "reservation" in wait_str.lower():
        return 10 # Assuming reservation is short time wait
    elif any(x in wait_str.lower() for x in ["60+", "long"]):
        return 60
    elif any(x in wait_str.lower() for x in ["30", "medium"]):
        return 30
    elif any(x in wait_str.lower() for x in ["short", "10-20", "no wait"]):
        return 15
    return 0


def process_cuisine(cuisine_str):
    return [c.strip() for c in cuisine_str.split(",")]


def get_price_value(price_symbol):
    price_map = {
        "$": 7500,
        "$$": 15000,
        "$$$": 25000,
        "$$$$": 40000
    }
    return price_map.get(price_symbol, 10000)  # Default to 10000 if symbol not found

# Process the data using the transformation functions
processed_data = []
for restaurant in data:
    processed_restaurant = {
        "name": restaurant["Name"],
        "cuisine": process_cuisine(restaurant["Cuisine"]),
        "diet": process_dietary(restaurant["Dietary"]),
        "payment": process_payment(restaurant["Payment"]),
        "rating": restaurant["Rating"],
        "num_ratings": restaurant["NumReviews"],
        "distance": restaurant["Distance_km"],
        "price": get_price_value(restaurant["Price"]),
        "wait": process_wait_time(restaurant["WaitTime"]),
        "englishfriendly": restaurant["EnglishFriendly"]
    }
    processed_data.append(processed_restaurant)

# Create DataFrame with processed data
restaurant_df = pd.DataFrame(processed_data)