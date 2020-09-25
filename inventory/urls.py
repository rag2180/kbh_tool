from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^products', products, name="products"),
    url(r'^add_product', add_product, name="add_product"),
    url(r'^(?P<product_id>\d+)$', product_detail, name="product_detail"),
    url(r'^product/(?P<product_id>\d+)/edit/', edit_product, name="edit_product"),
    url(r'^product/(?P<product_id>\d+)/delete/', delete_product, name="delete_product"),

    url(r'^ingredients', ingredients, name="ingredients"),
    url(r'^add_ingredient', add_ingredient, name="add_ingredient"),
    url(r'^ingredient/(?P<ingredient_id>\d+)/edit/', edit_ingredient, name="edit_ingredient"),
    url(r'^ingredient/(?P<ingredient_id>\d+)/delete/', delete_ingredient, name="delete_ingredient"),

    url(r'^overheads', overheads, name="overheads"),
    url(r'^add_overhead', add_overhead, name="add_overhead"),
    url(r'^overhead/(?P<overhead_id>\d+)/edit/', edit_overhead, name="edit_overhead"),
    url(r'^overhead/(?P<overhead_id>\d+)/delete/', delete_overhead, name="delete_overhead"),

    url(r'^customers', customers, name="customers"),
    url(r'^add_customer', add_customer, name="add_customer"),
    url(r'^edit_customer/(?P<customer_id>\d+)/edit/', edit_customer, name="edit_customer"),
    url(r'^delete_customer/(?P<customer_id>\d+)/delete/', delete_customer, name="delete_customer"),
    url(r'^customer/(?P<customer_id>\d+)/', customer_detail, name="customer_detail"),

    url(r'^categories', categories, name="categories"),
    url(r'^add_categories', add_category, name="add_category"),
    url(r'^category/(?P<category_id>\d+)/edit/', edit_category, name="edit_category"),
    url(r'^category/(?P<category_id>\d+)/delete/', delete_category, name="delete_category"),

    url(r'^orders', orders, name="orders"),
    url(r'^add_order', add_order, name="add_order"),
    url(r'^(?P<order_id>\d+)$', order_detail, name="order_detail"),
    url(r'^order/(?P<order_id>\d+)/edit/', edit_order, name="edit_order"),
    url(r'^order/(?P<order_id>\d+)/delete/', delete_order, name="delete_order"),
    ]
