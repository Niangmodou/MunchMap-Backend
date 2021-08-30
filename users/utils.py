from .serializers import AppUserSerializer


def custom_jwt_response_handler(token, user=None, request=None):
    return {
        "token": token,
        "user": AppUserSerializer(user, context={"request": request}).data,
    }
