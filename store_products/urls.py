from django.urls import path, re_path
from store_products.views import ProductDetailsView, ProductsGridView, sub_categories

app_name = 'store'

urlpatterns = (
    path('', ProductsGridView.as_view(), name='products grid'),
    path('<slug:slug>', ProductDetailsView.as_view(), name='product details'),
    path('<slug:subcategory_slug>/', sub_categories, name='subcategory list'),
)
