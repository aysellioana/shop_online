from shop.models import Category, CartItem
from shop.views import get_open_cart


def provide_navbar_data(request):
    main_categorys = Category.objects.filter(parent_category=None)
    all_categorys = Category.objects.all()
    if request.user.is_authenticated:
        open_cart = get_open_cart(request)
        cart_items = CartItem.objects.filter(cart=open_cart)
        cart_item_count = cart_items.count()
    else:
        cart_item_count = 0
    return {"main_categorys": main_categorys, "all_categorys": all_categorys, 'cart_item_count': cart_item_count}