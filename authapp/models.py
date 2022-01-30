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


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'X'

    GENDER_CHOICES = (
        (MALE, 'Man'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Nonbinary'),
    )

    user = models.OneToOneField(ShopUser, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='tags', max_length=50, blank=True)
    about_user = models.TextField(max_length=250, verbose_name='About me', blank=True)
    gender = models.CharField(verbose_name='gender', max_length=1, choices=GENDER_CHOICES, blank=True)