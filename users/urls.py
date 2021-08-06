from django.urls import include, path
from users import views

urlpatterns = [
    path('', views.index, name='index')
]