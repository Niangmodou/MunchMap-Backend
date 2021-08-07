import django
import os

# Configuring Django Settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from restaurants.models import Category, Restaurant

from restaurants.utils import add_restaurants_to_db, add_categories_to_db
