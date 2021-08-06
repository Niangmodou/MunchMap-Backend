from django.http import JsonResponse, HttpRequest

# Create your views here.
def index(request: HttpRequest) -> JsonResponse: 
    message: str = 'Hello MunchMap from Django Restaurants'
    return JsonResponse({'data': message})