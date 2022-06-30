from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from store_products.models import Product
# from django.views import generic as views



def cart_summary(request):
    return render(request, 'shopping_cart/summary.html')


def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product_price = request.POST.get('productprice')
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty, price=product_price)
        
        response = JsonResponse({'qty': product_qty, 'price': product_price})
        return response