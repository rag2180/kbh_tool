from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product, Ingredient, OverheadItem, Customer
from .forms import IngredientForm, OverheadItemForm, CustomerForm
from datetime import datetime

def home(request):
    return render(request, 'index.html', {})


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def ingredients(request):
    ingredients = Ingredient.objects.all()
    context = {'ingredients': ingredients}
    return render(request, 'ingredients.html', context)


def overheads(request):
    overheads = OverheadItem.objects.all()
    context = {'overheads': overheads}
    return render(request, 'overheads.html', context)


def customers(request):
    print("inside customers")
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})


def add_product(request):
    return render(request, "add_product.html", context={})


def edit_product(request, product_id):
    return render(request, "add_product.html", context={})


def add_ingredient(request):
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
                ingredient_form.save()
        else:
            print("INGREDIENT NOT VALID")
            return render(request, 'add_ingredients.html', {'alert': True, 'ingredient_form': ingredient_form})

    ingredient_form = IngredientForm()
    return render(request, 'add_ingredients.html', {'ingredient_form': ingredient_form})


def add_customer(request):
    print("inside add_customer - {}".format(request))
    if request.method == 'POST':
        print("Post Request")
        customer_form = CustomerForm(request.POST)
        # print(product_form)
        print(customer_form.is_valid())
        if customer_form.is_valid():
            print("Form is Valid")
            print(customer_form.cleaned_data)
            customer_name = customer_form.cleaned_data['name']
            phone_number = customer_form.cleaned_data['phone_number']
            address = customer_form.cleaned_data['address']
            city = customer_form.cleaned_data['city']
            email_id = customer_form.cleaned_data['email_id']
            date = datetime.now()
            customer = Customer.objects.create(name=customer_name, phone_number=phone_number,
                                             address=address, email_id=email_id,
                                             city=city, date=date)
            print(customer)
            return redirect("customers")
        else:
            customer_form = CustomerForm()
            return render(request, 'add_customer.html',
                          {'alert': True, 'customer_form': customer_form})

    else:
        customer_form = CustomerForm()

    return render(request, 'add_customer.html', {'customer_form': customer_form})


def edit_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST, instance=ingredient)
        if ingredient_form.is_valid():
            ingredient = ingredient_form.save(commit=False)
            ingredient.save()
            # redirect_path = '/ingredients_and_overheads/'.format(ingredient.id)
            return redirect('ingredient')
    else:
        ingredient_form = IngredientForm(instance=ingredient)

    return render(request, 'add_ingredients.html', {'ingredient_form': ingredient_form})


def edit_customer(request, customer_id):
    print("inside edit customer")
    customer = get_object_or_404(Customer, id=customer_id)
    print(customer)
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            ingredient = customer_form.save(commit=False)
            ingredient.save()
            return redirect("customers")
    else:
        customer_form = CustomerForm(instance=customer)

    return render(request, 'add_customer.html', {'customer_form': customer_form})


def add_overhead(request):
    if request.method == "POST":
        overhead_form = OverheadItemForm(request.POST)
        if overhead_form.is_valid():
                overhead_form.save()
        else:
            print("Overhead NOT VALID")
            return render(request, 'add_overhead.html', {'alert': True, 'overhead_form': add_overhead})

    overhead_form = OverheadItemForm()
    return render(request, 'add_overhead.html', {'overhead_form': overhead_form})


def edit_overhead(request, overhead_id):
    overhead = get_object_or_404(OverheadItem, id=overhead_id)
    if request.method == "POST":
        overhead_item_form = OverheadItemForm(request.POST, instance=overhead)
        if overhead_item_form.is_valid():
            overhead = overhead_item_form.save(commit=False)
            overhead.save()
            return redirect('overheads')
    else:
        overhead_item_form = OverheadItemForm(instance=overhead)

    return render(request, 'add_overhead.html', {'overhead_item_form': overhead_item_form})