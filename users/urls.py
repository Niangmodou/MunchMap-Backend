from django.urls import include, path
from users import views
from rest_framework_jwt.views import obtain_jwt_token
from .views import current_user, CreateUserView

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", obtain_jwt_token, name="login"),  # login a user
    path("currentuser/", current_user, name="current_user"),  # retrieve logged-in user
    path("signup/", CreateUserView.as_view(), name="sign_up"),  # sign-up
]
