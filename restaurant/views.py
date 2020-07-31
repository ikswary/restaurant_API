import json

from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import Restaurant, Menu


class RestaurantView(View):
    def post(self, request):
        data = json.loads(request.body)

        restaurant = Restaurant.objects.create(**data)
        return JsonResponse(restaurant.to_json('id', 'name', 'description', 'address', 'phone_number'), status=201)

    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.prefetch_related('menu_set').get(id=restaurant_id)
            restaurant_info = restaurant.to_json('id', 'name', 'description', 'address', 'phone_number')
            restaurant_info['menus'] = restaurant.get_menu_list()

            return JsonResponse(restaurant_info, status=200)

        except Restaurant.DoesNotExist:
            return HttpResponse(status=400)


class RestaurantListView(View):
    def get(self, request, page=1):
        restaurants = Restaurant.objects.all()[(page - 1) * 20:page + 20]
        restaurant_list = [restaurant.to_json('id', 'name', 'address', 'phone_number') for restaurant in restaurants]

        return JsonResponse({'list': restaurant_list}, status=200)


class MenuView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            menu = Menu.objects.create(**data)
            return JsonResponse(menu.to_json('id', 'name', 'price'), status=201)
        except ValueError:
            return HttpResponse(status=400)
        except IntegrityError:
            return HttpResponse(status=400)
