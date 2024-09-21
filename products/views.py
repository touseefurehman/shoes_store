from django.shortcuts import render
from .models    import Product,ItemCategory
# Create your views here.
def home(request):
    items_cate= ItemCategory.objects.all()
    products = Product.objects.all()

    return render(request, 'home.html',{'products': products,'items_cate': items_cate  })