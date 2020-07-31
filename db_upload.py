import os
from random import randint

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_API.settings")

import django

django.setup()
from restaurant.models import *

name_list = ['한식', '중식', '일식', '양식', '인도요리']

for name in name_list:
    for i in range(1, 11):
        restaurant = Restaurant(
            name=f'구의 {name} {i}호점',
            address=f'광진구 구의동 {randint(1, 999)}-{randint(1, 99)}',
            description='설명',
            phone_number=f'010-{randint(1, 9999)}-{randint(1, 9999)}'
        )
        restaurant.save()

        for j in range(1, 11):
            Menu(
                restaurant=restaurant,
                name=f'{name} 메뉴 {j}',
                price=randint(50, 99) * 100
            ).save()

    print(name)