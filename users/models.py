from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from restaurants.models import Restaurant

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length=100)

    owner = models.ForeignKey("AppUser", on_delete=models.CASCADE, related_name="collection")

    restaurants = models.ManyToManyField(Restaurant, blank=True)

    def __str__(self):
        return "{}".format(collection_name)
        
class AppUser(AbstractBaseUser):
    # Username, first_name, last_name, password, email, date_joined are stored in the AbstractUser type
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)

    collections =  models.ManyToManyField(Collection, blank=True)

    def __str__(self):
        return "{}".format(self.username)

