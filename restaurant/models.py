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


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField()

    class Meta:
        db_table = 'menus'
