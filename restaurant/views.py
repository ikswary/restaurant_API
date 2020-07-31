import json

from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import Restaurant, Menu


class RestaurantView(View):
    def post(self, request):
        try:
            key_requirements = ('name', 'description', 'address', 'phone_number')
            data = json.loads(request.body)

            for key in key_requirements:
                if not data[key]:
                    return HttpResponse(status=400)

            restaurant = Restaurant.objects.create(**data)
            return JsonResponse(restaurant.to_json('id', 'name', 'description', 'address', 'phone_number'), status=201)
        except KeyError:
            return HttpResponse(status=400)

    def get(self, request, restaurant_id=0):
        try:
            restaurant = Restaurant.objects.prefetch_related('menu_set').get(id=restaurant_id)
            restaurant_info = restaurant.to_json('id', 'name', 'description', 'address', 'phone_number')
            restaurant_info['menus'] = restaurant.get_menu_list()

            return JsonResponse(restaurant_info, status=200)

        except Restaurant.DoesNotExist:
            return HttpResponse(status=400)


class RestaurantListView(View):
    NUMBER_IN_PAGE = 20

    def get(self, request, page=1):
        offset = (page - 1) * self.NUMBER_IN_PAGE
        restaurants = Restaurant.objects.all()[offset:offset + self.NUMBER_IN_PAGE]
        restaurant_list = [restaurant.to_json('id', 'name', 'address', 'phone_number') for restaurant in restaurants]

        return JsonResponse({'list': restaurant_list}, status=200)


class MenuView(View):
    def post(self, request):
        try:
            key_requirements = ('restaurant_id', 'name', 'price')
            data = json.loads(request.body)

            for key in key_requirements:
                if not data[key]:
                    return HttpResponse(status=400)

            menu = Menu.objects.create(**data)
            return JsonResponse(menu.to_json('id', 'name', 'price'), status=201)
        except ValueError:
            return HttpResponse(status=400)
        except IntegrityError:
            return HttpResponse(status=400)
