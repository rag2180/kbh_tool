from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Product, Ingredient, OverheadItem, Customer, Category, ProductIngredient, ProductOverhead
from .forms import IngredientForm, OverheadItemForm, CustomerForm, CategoryForm, ProductForm,ProductIngredientForm
from datetime import datetime
from django.forms import inlineformset_factory, modelformset_factory

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


def categories(request):
    print("inside customers")
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def add_product(request):
    if request.method == 'POST':
        print("Post Request")
        print(request.POST)
        # # print(product_form)
        # print(product_form.is_valid())
        # if product_form.is_valid():
        #     print("Form is Valid")
        #     print(product_form.cleaned_data)
        #     product_name = product_form.cleaned_data['name']
        #     product_category = product_form.cleaned_data['category']
        #     profit_percent = product_form.cleaned_data['profit_percent']
        #     note = product_form.cleaned_data['note']
        #     product = Product.objects.create(name=product_name, category=product_category, profit_percent=profit_percent,
        #                                   note=note)
        #     print(product)
        #     redirect_path = 'add_ingredient_of_product/{}'.format(product.id)
        #     return redirect(redirect_path, product_id=product.id)
        # else:
        #     product_form = ProductForm()
        #     return render(request, 'add_product.html', {'alert': True, 'product_form': product_form})

    else:
        product_form = ProductForm()
        ingredient_form = ProductIngredientForm()
        return render(request, 'add_product.html', {'product_form': product_form, 'ingredient_form': ingredient_form})


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


def add_category(request):
    print("creating categories")
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
        else:
            print("form is not valid")
            return render(request, 'add_category.html',
                          {'alert': True, 'category_form': category_form})
        return redirect('add_category')

    category_form = CategoryForm()
    return render(request, 'add_category.html', {'category_form': category_form})


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
            return redirect('ingredients')
    else:
        ingredient_form = IngredientForm(instance=ingredient)

    return render(request, 'add_ingredients.html', {'ingredient_form': ingredient_form})


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    print(category)
    if request.method == "POST":
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.save()
            redirect_path = 'categories'
            return redirect(redirect_path)
    else:
        category_form = CategoryForm(instance=category)

    return render(request, 'add_category.html', {'category_form': category_form})



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


def customer_detail(request, customer_id):
    print("Inside customer detail")
    customer = get_object_or_404(Customer, id=customer_id)
    # TODO: Show all past orders by this customer
    return render(request, 'customer_detail.html', {'customer': customer})


def product_detail(request, product_id):
    """
    Product Detail Page
    :param request:
    :param pk:
    :return:
    """
    product = get_object_or_404(Product, pk=product_id)
    all_product_ingredients = ProductIngredient.objects.filter(product=product)
    all_product_overheads = ProductOverhead.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product,
                                                               'ingredients': all_product_ingredients,
                                                               'overheads': all_product_overheads})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("ingredients")

    context = {"obj": product, "type": "product"}
    return render(request, "delete_ingredient.html", context)


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        customer.delete()
        return redirect("customers")

    context = {"obj": customer, "type": "customer"}
    return render(request, "delete_ingredient.html", context)


def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == "POST":
        ingredient.delete()
        return redirect("ingredients")

    context = {"obj": ingredient, "type": "ingredient"}
    return render(request, "delete_ingredient.html", context)


def delete_overhead(request, overhead_id):
    overhead = get_object_or_404(OverheadItem, id=overhead_id)
    if request.method == "POST":
        overhead.delete()
        return redirect("overheads")

    context = {"obj": overhead, "type": "overhead"}
    return render(request, "delete_ingredient.html", context)


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
        return redirect("categories")

    context = {"obj": category, "type": "category"}
    return render(request, "delete_ingredient.html", context)