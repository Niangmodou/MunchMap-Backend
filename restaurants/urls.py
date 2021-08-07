from django.urls import include, path
from restaurants import views

urlpatterns = [path("", views.index, name="index")]
