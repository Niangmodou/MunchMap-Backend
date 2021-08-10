from rest_framework.serializers import ModelSerializer

from .models import AppUser, Collection


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"


class UserSerializer(ModelSerializer):
    collections = CollectionSerializer(many=True, read_only=True)
    
    class Meta:
        model = AppUser
        fields = "__all__"

