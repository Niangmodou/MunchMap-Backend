<<<<<<< HEAD
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.settings import api_settings
from .models import AppUser, Collection
from rest_framework import serializers
=======
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import AppUser

>>>>>>> workinglogin

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("username", "email", "full_name", "zipcode", "collections")


class AppUserRegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)

        return token

    def create(self, validated_data):
        user = AppUser.objects.create(
            username=validated_data["username"],
            full_name=validated_data["full_name"],
            email=validated_data["email"],
            zipcode=validated_data["zipcode"],
        )
        password = validated_data["password"]

        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = AppUser
        fields = (
            "token",
            "username",
            "email",
            "password",
            "full_name",
            "zipcode",
            "collections",
        )
