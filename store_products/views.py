from decimal import Decimal
from django.http import HttpResponse
from django.views import generic as views
from django.shortcuts import get_object_or_404, render
from store_products.models import Category, Product, SubCategory
from rating_section.forms import CommentForm
import json

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def sub_categories(request, subcategory_slug=None):
    sub_category = get_object_or_404(SubCategory, slug=subcategory_slug)
    products = Product.objects.filter(subcategory=sub_category)
    return render(request, 'store_products/products_grid.html', {'sub_category': sub_category, 'products': products})

class ProductsGridView(views.ListView):
    model = Product
    template_name = 'store_products/products_grid.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         bestsellers =  Product.objects.all().order_by('-sales')
         
         context.update({
             'bestsellers': bestsellers,
         })
         return context



class ProductDetailsView(views.DetailView):
     model = Product
     template_name = 'store_products/product_details.html'
     context_object_name = 'product'
     
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         
         if self.object.size:
            sizes = list(self.object.size.all())
         else:
             sizes = None

         if self.object.discount:
            discount = self.object.price * Decimal(self.object.discount / 100)
         else:
            discount = 0
            
         price_with_discount = self.object.price - discount
         
         product = context['product']
         reviews_count = len(product.comment_set.all())
         context['comment_form'] = CommentForm(
             initial={'product_slug': self.object.slug,}
         )
         context['comments'] = product.comment_set.all()
         
         context.update({
             'sizes': sizes,
             'price_with_discount': price_with_discount,
             'reviews_count': reviews_count,
         })
         return context
         
