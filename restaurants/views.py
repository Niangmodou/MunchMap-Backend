from django.http import JsonResponse, HttpRequest

from restaurants.models import Restaurant, Category
from restaurants.serializers import RestaurantSerializer

from users.models import AppUser

# Create your views here.
def index(request: HttpRequest) -> JsonResponse:
    message: str = "Hello MunchMap from Django Restaurants"
    return JsonResponse({"data": message})


def all_restaurants(request: HttpRequest) -> JsonResponse:
    restaurants = Restaurant.objects.all()

    result = []
    for restaurant in restaurants:
        result.append(RestaurantSerializer(restaurant).data)

    parameter_dict = {"code": 200, "status": "success", "restaurants": result}

    return JsonResponse({"data": parameter_dict})
