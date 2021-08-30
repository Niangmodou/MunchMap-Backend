from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.http import HttpResponseRedirect

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AppUserRegistrationSerializer, AppUserSerializer
from .models import AppUser

# Create your views here.
def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"data": "Hello MunchMap from Django Users"})


@api_view(["GET"])
def current_user(request: HttpRequest) -> JsonResponse:
    serialzer = AppUserSerializer(request.user)

    return JsonResponse(serialzer.data)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request: HttpRequest):
        user = request.data

        if not user:
            return JsonResponse({"response": "error", "message": "No Data"})

        serializer = AppUserRegistrationSerializer(data=user)

        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse({"response": "error", "message": serializer.errors})

        return JsonResponse(
            {"response": "success", "message": "user created succesfully"}
        )
