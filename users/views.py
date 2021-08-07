from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

# Create your views here.
def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"data": "Hello MunchMap from Django Users"})
