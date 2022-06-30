from csv import list_dialects
from django.contrib import admin
from store_products.models import Category, ProductSizeChoice, Product, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    

@admin.register(ProductSizeChoice)
class ProductSizeChoiceAdmin(admin.ModelAdmin):
    list_display = ('size_choice',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price', 'in_stock', 'quantity')
    
   