from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product


def get_category_menu():
    return ProductCategory.objects.all()


def index(request):
    context = {
        'page_title': 'OxENGLISH Book Shop',
        'category_menu': get_category_menu(),
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    context = {
        'page_title': 'OxENGLISH Textbooks',
        'category_menu': get_category_menu(),
    }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    context = {
        'page_title': 'OxENGLISH Contact',
        'category_menu': get_category_menu(),
    }
    return render(request, 'mainapp/contact.html', context=context)


def category_items(request, category_pk):
    if category_pk == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=category_pk)

    context = {
        'page_title': 'Category',
        'category_menu': get_category_menu(),
        'products': products,
        'category_pk': category_pk,
    }
    return render(request, 'mainapp/category_items.html', context)


def product_page(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    context = {
        'page_title': 'Product',
        'category_menu': get_category_menu(),
        'product': product,
        'category_pk': product.category_id,
    }
    return render(request, 'mainapp/product_page.html', context)

