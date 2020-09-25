from django.contrib import admin

from .models import Customer, Category, Ingredient, OverheadItem, Product, Order, OrderItem

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(OverheadItem)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
