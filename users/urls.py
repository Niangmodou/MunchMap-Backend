from django.urls import include, path
from users import views


urlpatterns = [
    path("", views.index, name="index"),
    path("current_user", views.current_user),
    path("users", views.UserList.as_view()),
]
