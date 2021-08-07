import django
import os

# Configuring Django Settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from restaurants.models import Category, Restaurant


def add_categories_to_db(category_name: str) -> Category:
    return Category.objects.create(category_name=category_name)


def add_restaurants_to_db(
    restaurant: str, category: Category, address: str, latitude: float, longitude: float
) -> Restaurant:
    restaurant_obj = Restaurant.objects.create(
        restaurant_name=restaurant,
        business_address=address,
        latitude=latitude,
        longitude=longitude,
    )

    restaurant_obj.category.add(category)

    return restaurant_obj
