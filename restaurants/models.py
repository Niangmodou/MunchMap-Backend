from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return "{}".format(self.category_name)


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)

    category = models.ManyToManyField(Category, blank=True)

    business_address = models.CharField(max_length=200)

    latitude = models.DecimalField(max_digits=17, decimal_places=14)
    longitude = models.DecimalField(max_digits=17, decimal_places=14)

    def __str__(self):
        return "{}".format(self.restaurant_name)
