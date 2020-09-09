from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^products', products, name="products"),
    url(r'^product/(?P<product_id>\d+)/edit/', edit_product, name="edit_product"),
    url(r'^add_product', add_product, name="add_product"),

    url(r'^ingredients', ingredients, name="ingredients"),
    url(r'^add_ingredient', add_ingredient, name="add_ingredient"),
    url(r'^ingredient/(?P<ingredient_id>\d+)/edit/', edit_ingredient, name="edit_ingredient"),

    url(r'^overheads', overheads, name="overheads"),
    url(r'^add_overhead', add_overhead, name="add_overhead"),
    url(r'^overhead/(?P<overhead_id>\d+)/edit/', edit_overhead, name="edit_overhead"),

    url(r'^customers', customers, name="customers"),
    url(r'^add_customer', add_customer, name="add_customer"),
    url(r'^edit_customer/(?P<customer_id>\d+)/edit/', edit_customer, name="edit_customer"),
    ]
