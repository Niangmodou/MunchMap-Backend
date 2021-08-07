import django
import os

# Configuring Django Settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

import requests
import json
from restaurants.models import Category, Restaurant
import pandas as pd
from restaurants.utils import add_restaurants_to_db, add_categories_to_db

URL = "https://api.yelp.com/v3/businesses/"


def query_restaurant(business_id: str) -> dict:
    """
    make api call for restaurant and return json data
    """
    request_url = URL + business_id

    response = requests.get(
        request_url,
        headers={
            "Authorization": "Bearer eczkFIwLglZ5FqMM9CIXLwHTCHRcHtSUvQmuJ4v10clfAGKhAERRSZ0MrvJ-UfVc7oo1nSrbjHWe27VIOUIdmwu1sYhsgJFgYONhWZKaKHqDDqs9aMMxLBatbdkNYXYx"
        },
    )

    data = response.json()

    return data


def add_category(category: str) -> Category:
    """
    checks if a category is in database and adds
    """
    if not Category.objects.filter(category_name=category).exists():
        return add_categories_to_db(category)

    return None


def parse_restaurant_data(data: dict) -> Restaurant:
    """
    parse restaurant json data & add to database
    """
    category = add_category(data["categories"][0]["title"])

    name = data["name"]

    business_address = " ".join(list(data["location"]["display_address"]))

    latitude = data["coordinates"]["latitude"]
    longitude = data["coordinates"]["longitude"]

    restaurant_obj = add_restaurants_to_db(
        name, category, business_address, latitude, longitude
    )

    for idx in range(1, len(data["categories"])):
        cat_name = data["categories"][idx]["title"]
        print(
            "{} {} {} {} {}".format(
                name, cat_name, business_address, latitude, longitude
            )
        )
        category = add_category(cat_name)

        if category != None:
            restaurant_obj.category.add(category)

    return restaurant_obj


def retrieve_restaurant_ids() -> list:
    """
    reads csv data and retrieve Manhattan restaurant ids
    """
    data = pd.read_csv("manhattan_data.csv")

    manhattan_data = data[data["city"] == "New York"]

    business_ids = manhattan_data["id"]

    return business_ids


def main():
    restaurant_ids = retrieve_restaurant_ids()

    for business_id in restaurant_ids:
        try:
            data = query_restaurant(business_id)

            parse_restaurant_data(data)
        except Exception:
            continue

    print(len(Category.objects.all()))
    print(len(Restaurant.objects.all()))

    print(Category.objects.all())
    print(Restaurant.objects.all())


if __name__ == "__main__":
    main()
