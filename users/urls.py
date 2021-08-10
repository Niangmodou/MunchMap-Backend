from django.urls import include, path
from users import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [path("", views.index, name="index"),]
