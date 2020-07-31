from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=500, null=False)

    class Meta:
        db_table = 'restaurants'

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "phone_number": self.phone_number
        }
    def get_restaurant_list(self):
        return [{'id': restaurant.id,
                 'name': restaurant.name,
                 'price': restaurant.address,
                 'phone_number': restaurant.phone_number} for restaurant in self.objects.all()]

    def get_menu_list(self):
        return [{'id': menu.id,
                 'name': menu.name,
                 'price': menu.price} for menu in self.menu_set.all()]

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField()

    class Meta:
        db_table = 'menus'

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
