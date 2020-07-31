import json

from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import Restaurant


class RestaurantView(View):
    def post(self, request):
        data = json.loads(request.body)

        restaurant = Restaurant.objects.create(**data)
        return JsonResponse(restaurant.to_json(), status=201)
