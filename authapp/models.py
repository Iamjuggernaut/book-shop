from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.db import models
from django.utils import timezone


def default_exp_date():
    return timezone.now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    # activation_key = models.CharField(verbose_name='activation key', max_length=50, null=True)
    # activation_expires = models.DateTimeField(verbose_name='expiration date', default=default_exp_date)


    # def is_activation_key_expired(self):
    #     return self.activation_expires > timezone.now()


    def basket_total_cost(self):
        return sum(map(lambda x: x.product_cost, self.basket.all()))

    def basket_total_qty(self):
        return sum(map(lambda x: x.quantity, self.basket.all()))