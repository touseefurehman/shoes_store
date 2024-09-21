# Generated by Django 5.1.1 on 2024-09-19 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category_of_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category_of_items',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.itemcategory'),
        ),
    ]