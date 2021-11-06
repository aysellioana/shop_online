from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from shop.forms import ClientForm, UserForm
from shop.models import *


def home(request):
    main_categorys = Category.objects.filter(parent_category=None)
    all_categorys = Category.objects.all()
    return render(request, "home.html", {"main_categorys": main_categorys, "all_categorys": all_categorys})


def open_cart_view(request):
    open_cart = get_open_cart(request)
    cart_items = CartItem.objects.filter(cart=open_cart)
    return render(request, "open_cart.html", {"open_cart": open_cart, "cart_items": cart_items})


def get_open_cart(request):
    user = request.user
    client = Client.objects.get(user=user)
    open_carts = Cart.objects.filter(client=client, status="open")
    if open_carts.count() > 0:
        open_cart = open_carts.first()
    else:
        open_cart = Cart.objects.create(client=client)
    return open_cart


def add_product_to_cart(request):
    open_cart = get_open_cart(request)
    product_id = request.POST.get("product_id", None)
    quantity = request.POST.get("quantity", 1)
    if product_id is not None:
        existing_cart_items = CartItem.objects.filter(cart=open_cart, product_id=product_id)
        if existing_cart_items.count() > 0:
            existing_cart_item = existing_cart_items.first()
            existing_cart_item.quantity += quantity
            existing_cart_item.save()
        else:
            existing_cart_item = CartItem.objects.create(cart=open_cart, product_id=product_id, quantity=quantity)
        if existing_cart_item.quantity < 1:
            existing_cart_item.delete()
    return redirect(reverse_lazy("open_cart"))


def registration_view(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save()
            client.user = user
            client.save()
            return redirect(reverse_lazy('login'))
    else:
        user_form = UserForm()
        client_form = ClientForm()

    return render(request, 'registration.html', {'user_form': user_form, 'client_form': client_form})
