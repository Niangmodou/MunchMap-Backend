from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
from django.utils import timezone
from restaurants.models import Restaurant

from .managers import CustomUserManager

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length=100)

    owner = models.ForeignKey(
        "AppUser", on_delete=models.CASCADE, related_name="collection"
    )

    restaurants = models.ManyToManyField(Restaurant, blank=True)

    def __str__(self):
        return "{}".format(collection_name)


class AppUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)

    collections = models.ManyToManyField(Collection, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return "{}".format(self.username)
