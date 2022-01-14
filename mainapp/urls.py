from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.index, name='index'),
    path('products/', mainapp.products, name='products'),
    path('category/<int:category_pk>/', mainapp.category_items, name='category_items'),
    path('product/<int:product_pk>/', mainapp.product_page, name='product_page'),
    path('contact/', mainapp.contact, name='contact'),
]
