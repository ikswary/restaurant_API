import json

from django.http import JsonResponse
from django.views import View

from .models import Restaurant, Menu


class RestaurantView(View):
    def post(self, request):
        data = json.loads(request.body)

        restaurant = Restaurant.objects.create(**data)
        return JsonResponse(restaurant.to_json(), status=201)


class MenuView(View):
    def post(self, request):
        data = json.loads(request.body)

        menu = Menu.objects.create(**data)
        return JsonResponse(menu.to_json(), status=201)



