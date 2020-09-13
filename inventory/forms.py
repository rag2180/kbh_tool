from django.forms import ModelForm
from .models import Product, OrderItem, Category, Ingredient, OverheadItem, ProductIngredient, ProductOverhead, Customer, Order
from django.forms import modelformset_factory
from django.forms import formset_factory
from django import forms


class ProductForm(ModelForm):
    # prefix = 'product'

    class Meta:
        model = Product
        fields = ['name', 'category', 'profit_percent', 'note']


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class CategoryForm(ModelForm):
    prefix = 'category'

    class Meta:
        model = Category
        fields = '__all__'


class OverheadItemForm(ModelForm):
    class Meta:
        model = OverheadItem
        fields = '__all__'


class ProductIngredientForm(ModelForm):
    class Meta:
        model = ProductIngredient
        fields = ['ingredient', 'quantity']


class ProductOverheadForm(ModelForm):
    class Meta:
        model = ProductOverhead
        fields = '__all__'


# ProductIngredientFormset = modelformset_factory(
#     ProductIngredientForm,
#     fields=('ingredient', 'quantity',)
# )

#ProductFormset = formset_factory(ProductForm, extra=1)


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = ['customer', 'delivery_status', 'payment_status', 'note_from_customer']
#
#
# class OrderItemForm(ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = '__all__'
#


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'