from django.shortcuts import render
from django.views import generic as views
from store_products.models import Product



class HomePageView(views.ListView):
    template_name = 'main/homepage.html'
    queryset = Product
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         products_on_sale =  Product.objects.all().filter(on_sale=True)
         
         context.update({
             'products_on_sale': products_on_sale,
         })
         return context