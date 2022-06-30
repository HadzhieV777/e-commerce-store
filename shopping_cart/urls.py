from django.urls import path
from shopping_cart.views import cart_summary, add_to_cart

app_name = 'cart'

urlpatterns = (
    path('', cart_summary, name='cart summary'),
    path('add/', add_to_cart, name='add to cart'),
)





