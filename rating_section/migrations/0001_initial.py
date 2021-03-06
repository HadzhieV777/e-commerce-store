# Generated by Django 4.0.4 on 2022-05-10 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_products', '0006_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(max_length=25)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('text', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_products.product')),
            ],
        ),
    ]
