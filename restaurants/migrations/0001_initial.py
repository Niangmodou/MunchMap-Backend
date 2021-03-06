# Generated by Django 3.2.6 on 2021-08-07 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "category_name",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("restaurant_name", models.CharField(max_length=200)),
                ("business_address", models.CharField(max_length=200)),
                ("latitude", models.DecimalField(decimal_places=14, max_digits=17)),
                ("longitude", models.DecimalField(decimal_places=14, max_digits=17)),
                (
                    "category",
                    models.ManyToManyField(blank=True, to="restaurants.Category"),
                ),
            ],
        ),
    ]
