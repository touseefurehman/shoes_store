from django.shortcuts import render
from .models    import Product,ItemCategory
# Create your views here.
def home(request):
    items_cate= ItemCategory.objects.all()
    products = Product.objects.all()

    return render(request, 'home.html',{'products': products,'items_cate': items_cate  })


def product_grid(request):
    items_cate= ItemCategory.objects.all()
    products = Product.objects.all()

    return render(request, 'g.html',{'products': products,'items_cate': items_cate  })