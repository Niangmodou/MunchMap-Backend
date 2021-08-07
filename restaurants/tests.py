from django.test import TestCase

from restaurants.utils import add_restaurants_to_db, add_categories_to_db
from restaurants.models import Category, Restaurant

# Create your tests here.
class RestaurantTests(TestCase):
    def test_add_categories_to_db(self):
        # Asserting database is empty
        self.assertEqual(len(Category.objects.all()), 0)

        cat1 = add_categories_to_db("French")
        cat2 = add_categories_to_db("Italian")
        cat3 = add_categories_to_db("American")

        self.assertEqual(len(Category.objects.all()), 3)

    def test_add_restaurants_to_db(self):
        # Asserting database is empty
        self.assertEqual(len(Restaurant.objects.all()), 0)

        cat1 = add_categories_to_db("French")
        cat2 = add_categories_to_db("Italian")

        rest1 = add_restaurants_to_db("Cafe", cat1, "123 Avenue A", 54.2324, 43.435)
        rest2 = add_restaurants_to_db("Bistro", cat2, "1600 Penn Ave", 23.2324, 76.435)

        self.assertEqual(len(Restaurant.objects.all()), 2)

        self.assertEqual(rest1.restaurant_name, "Cafe")
        self.assertEqual(rest2.restaurant_name, "Bistro")
