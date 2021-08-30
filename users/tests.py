from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib import auth

from .models import AppUser

# Create your tests here.
class AuthTestCase(TestCase):
    def setUp(self):
        self.u = AppUser.objects.create_user(
            full_name="test@dom",
            email="test@dom.com",
            username="test@dom.com",
            password="pass",
            zipcode=10003,
        )
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username="test@dom.com", password="pass")


# class UserAccountTests(TestCase):
#     def test_create_new_user(self):
#         # Assert the database is empty
#         self.assertEqual(len(AppUser.objects.all()), 0)

#         user1 = AppUser.objects.create(
#             username = "TestUser1",
#             email = "TestUser1@gmail.com",
#             full_name = "Test User1",
#             zipcode = 10003
#         )

#         user2 = AppUser.objects.create(
#             username = "TestUser2",
#             email = "TestUser2@gmail.com",
#             full_name = "Test User2",
#             zipcode = 10003
#         )

#         user3 = AppUser.objects.create(
#             username = "TestUser3",
#             email = "TestUser3@gmail.com",
#             full_name = "Test User3",
#             zipcode = 10003
#         )

#         self.assertEqual(len(AppUser.objects.all()), 3)

#     def test_sign_up_user(self):
#         # Assert the database is empty
#         self.assertEqual(len(AppUser.objects.all()), 0)

#         client = Client()

#         # Make calls to signup route to add users
#         client.post(reverse("sign_up"), {"user": {
#             "username": "test1",
#             "password": "testpassword1",
#             "email": "Testemail1@gmail.com",
#             "full_name": "Test user1",
#             "zipcode": "10003"
#         }})

#         client.post(reverse("sign_up"), {"user": {
#             "username": "test2",
#             "password": "testpassword2",
#             "email": "Testemail2@gmail.com",
#             "full_name": "Test user2",
#             "zipcode": "10003"
#         }})

#         client.post(reverse("sign_up"), {"user": {
#             "username": "test3",
#             "password": "testpassword3",
#             "email": "Testemail3@gmail.com",
#             "full_name": "Test user3",
#             "zipcode": "10003"
#         }})

#         # Assert users are in database
#         self.assertEqual(len(AppUser.objects.all()), 3)

#     def test_login_user_api(self):
#         client = Client()

#         client.post(reverse("sign_up"), {"user": {
#             "username": "test3",
#             "password": "testpassword3",
#             "email": "Testemail3@gmail.com",
#             "full_name": "Test user4",
#             "zipcode": "10003"
#         }})

#         # Trying to log in
#         response = client.post(reverse("login"), {
#             "username": "test3",
#             "password": "testpassword3",
#         })

#         self.assertEqual(response.status_code, 200)

# def test_current_user_api(self):
#     client = Client()

#     client.post(reverse("sign_up"), {
#         "username": "test3",
#         "password": "testpassword3",
#         "email": "Testemail3@gmail.com",
#         "full_name": "Test user4",
#         "zipcode": "10003"
#     })

#     # Trying to log in
#     response = client.post(reverse("login"), {
#         "username": "test3",
#         "password": "testpassword3",
#     })

#     self.assertEqual(response.status_code, 200)

#     response = client.get(reverse("current_user"))

#     self.assertEqual(response.status_code, 200)

#     # Asserting logged in user is test3
#     token = response.data["token"]
#     current_user = Token.objects.get(key = token).user

#     self.assertEqual(current_user.username, "test3")
