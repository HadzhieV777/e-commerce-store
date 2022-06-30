from email.policy import default
from unicodedata import category
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager).get_queryset().filter(is_active=True)
    


class Category(models.Model):
    NAME_MAX_LEN = 255
    
    name = models.CharField(
        max_length= NAME_MAX_LEN,
        db_index=True,
    )
    slug = AutoSlugField(
        populate_from='name'
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    
    def __str__(self):
        return self.name    
    
    class Meta:
        ordering = ('created',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
   


class SubCategory(models.Model):
    NAME_MAX_LEN = 255
    
    name = models.CharField(
        max_length= NAME_MAX_LEN,
        db_index=True,
    )
    slug = AutoSlugField(
        populate_from='name'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name='product_subcategories',
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:subcategory list', args=[self.slug])
    
    class Meta:
        ordering = ('created',)
        verbose_name = 'sub-category'
        verbose_name_plural = 'sub-categories'

    
    
class ProductSizeChoice(models.Model):
    SIZE_CHOICE_MAX_LEN = 10
    
    size_choice=models.CharField(
        max_length=SIZE_CHOICE_MAX_LEN,
        unique=True,
    )
    
    class Meta:
        verbose_name_plural = 'Product Size'
        
    
    def __str__(self):
        return self.size_choice


class Product(models.Model):
    NAME_MAX_LEN = 80
    IMAGE_UPLOAD_TO_DIR = 'product_images/'
    PRICE_MAX_DIGITS = 5
    PRICE_DECIMAL_PLACES =2
    DEFAULT_IMAGE_DIR = 'product_images/default.png'
       
    subcategory=models.ForeignKey(
        SubCategory,
        related_name='product',
        on_delete=models.CASCADE,
        blank=True,
    )
    name=models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
    )
    excerpt = models.TextField(
        null=True,
    )
    description=models.TextField()
    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        default= DEFAULT_IMAGE_DIR,
    )
    slug = AutoSlugField(
        populate_from='name'
    )
    price=models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
    )
    size=models.ManyToManyField(
        ProductSizeChoice,
        blank=True,
    )
    in_stock=models.BooleanField(
        default=True,
    )
    quantity = models.IntegerField()
    is_active=models.BooleanField(
        default=True,
    )
    on_sale=models.BooleanField(
        default=False,
    )
    discount = models.IntegerField(
        null=True,
        blank=True,
    )
    sales = models.IntegerField(
        null=True,
        blank=True,
        default=0,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ["-created", "-updated"]
    
    def get_absolute_url(self):
        return reverse('store:product detail', args=[self.slug])
    
    def __str__(self):
        return self.name