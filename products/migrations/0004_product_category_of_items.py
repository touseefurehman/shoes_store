# Generated by Django 5.1.1 on 2024-09-19 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_itemcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Category_of_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='products.itemcategory'),
        ),
    ]
