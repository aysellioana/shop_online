from django.urls import path

from shop import views

urlpatterns = [
    path('', views.home, name='index'),
    path('open_cart', views.open_cart_view, name='open_cart'),
    path('add_product_to_cart', views.add_product_to_cart, name='add_product_to_cart'),
    path('registration', views.registration_view, name='registration'),
    path('category_details/<int:category_id>/', views.category_details_view, name='category_details'),
    path('profile', views.details_client, name='profile'),
    path('search', views.search_view, name='search'),
    path('wishlist', views.get_wishlist, name='wishlist'),
    path('update/<int:pk>/', views.ClientUpdateView.as_view(), name='update'),
    path('product_details/<int:product_id>/', views.product_details_view, name='product_details'),


]
