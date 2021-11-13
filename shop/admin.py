from django.contrib import admin

from shop.models import Client, Product, Category, CartItem, Cart, CarouselItem

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CarouselItem)

