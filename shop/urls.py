from django.urls import path

from shop import views

urlpatterns = [
    path('', views.home, name='index'),
    path('open_cart', views.open_cart_view, name='open_cart'),
    path('add_product_to_cart', views.add_product_to_cart, name='add_product_to_cart'),
    path('registration', views.registration_view, name='registration'),


]