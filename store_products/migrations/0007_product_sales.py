# Generated by Django 4.0.4 on 2022-05-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_products', '0006_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
