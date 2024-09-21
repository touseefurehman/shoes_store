from django.contrib import admin

# Register your models here.
from .models import Product , ItemCategory

admin.site.register(Product)

admin.site.register(ItemCategory)