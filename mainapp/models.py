from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Product type', max_length=50)
    description = models.TextField('Type description', blank=True, max_length=240)
    is_active = models.BooleanField('active', default=True)

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Product name', max_length=50)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField('Product description', blank=True, max_length=240)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2, default=0)
    short_description = models.CharField('Short description', max_length=50, blank=True)
    quantity = models.PositiveIntegerField('Amount', default=0)
    is_active = models.BooleanField('active', default=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} ({self.category.name})'