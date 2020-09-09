from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'index.html', {})


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def add_product(request):
    return render(request, "add_product.html", context={})


def edit_product(request, product_id):
    return render(request, "add_product.html", context={})
