import json

from django.http import JsonResponse
from django.views import View

from .models import Restaurant, Menu


class RestaurantView(View):
    def post(self, request):
        data = json.loads(request.body)

        restaurant = Restaurant.objects.create(**data)
        return JsonResponse(restaurant.to_json(), status=201)

    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.prefetch_related('menu_set').get(id=restaurant_id)
        restaurant_info = restaurant.to_json()
        restaurant_info['menus'] = restaurant.get_menu_list()

        return JsonResponse(restaurant_info, status=200)


class RestaurantListView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        restaurant_list = [restaurant.to_json() for restaurant in restaurants]

        return JsonResponse({'list': restaurant_list}, status=200)


class MenuView(View):
    def post(self, request):
        data = json.loads(request.body)

        menu = Menu.objects.create(**data)
        return JsonResponse(menu.to_json(), status=201)
