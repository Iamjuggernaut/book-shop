from django.db import models
from django.contrib.auth import get_user_model
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity', default=0)
    add_datetime = models.DateTimeField('Date:' ,auto_now_add=True)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @classmethod
    def get_items(self, user):
        return Basket.objects.filter(user=user)