from django.db import models
from store_products.models import Product


class Comment(models.Model):
    USER_NAME_MAX_LEN = 25
    
    published = models.DateTimeField(
        auto_now=True,
    )
    user_name = models.CharField(
        max_length=USER_NAME_MAX_LEN,
    )
    user_email = models.EmailField(
        null=True, 
        blank=True,
    )
    text = models.TextField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

