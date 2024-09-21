from django.db import models

# Category Model
class ItemCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_of_item/', blank=True, null=True)
    
    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, related_name="products", null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(blank=True, null=True, default=0)
    product_image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name
