from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):

    def basket_total_cost(self):
        return sum(map(lambda x: x.product_cost, self.basket.all()))

    def basket_total_qty(self):
        return sum(map(lambda x: x.quantity, self.basket.all()))