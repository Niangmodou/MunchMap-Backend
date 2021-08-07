from django.test import TestCase, Client
from django.urls import reverse

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


class RestaurantAPITests(TestCase):
    def setUp(self):
        self.client = Client()

        cat1 = add_categories_to_db("French")
        cat2 = add_categories_to_db("Italian")
        cat3 = add_categories_to_db("American")

        rest1 = add_restaurants_to_db("Cafe", cat1, "123 Avenue A", 54.2324, 43.435)
        rest2 = add_restaurants_to_db("Bistro", cat2, "1600 Penn Ave", 23.2324, 76.435)
        rest3 = add_restaurants_to_db("Burgers", cat3, "205 5th Ave", 123.043, 54.75)

    def test_fetch_all_restaurants(self):
        response = self.client.get(reverse("all_restaurants"))

        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertEqual(len(response_data["data"]), 3)

        # Assert names are equal
        self.assertEqual(
            response_data["data"]["restaurants"][0]["restaurant_name"], "Cafe"
        )
        self.assertEqual(
            response_data["data"]["restaurants"][1]["restaurant_name"], "Bistro"
        )
        self.assertEqual(
            response_data["data"]["restaurants"][2]["restaurant_name"], "Burgers"
        )

        # Assert categories are equal
        self.assertEqual(
            response_data["data"]["restaurants"][0]["category"][0]["category_name"],
            "French",
        )
        self.assertEqual(
            response_data["data"]["restaurants"][1]["category"][0]["category_name"],
            "Italian",
        )
        self.assertEqual(
            response_data["data"]["restaurants"][2]["category"][0]["category_name"],
            "American",
        )

        # Assert Lat and Lon are floats
        self.assertEqual(
            type(response_data["data"]["restaurants"][0]["latitude"]), float
        )
        self.assertEqual(
            type(response_data["data"]["restaurants"][0]["longitude"]), float
        )