from django.urls import include, path
from restaurants import views

urlpatterns = [
    path("", views.index, name="index"),
    path("allrestaurants", views.all_restaurants, name="all_restaurants"),
]
