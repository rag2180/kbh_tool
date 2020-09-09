from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^products', products, name="products"),
    url(r'^add_product', add_product, name="add_product"),
    url(r'^product/(?P<product_id>\d+)/edit/', edit_product, name="edit_product"),
    ]
