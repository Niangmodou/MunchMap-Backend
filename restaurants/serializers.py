from rest_framework.serializers import ModelSerializer

from .models import Restaurant, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RestaurantSerializer(ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"
