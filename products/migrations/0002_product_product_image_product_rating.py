# Generated by Django 5.1.1 on 2024-09-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to='products/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
