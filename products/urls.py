
from django.contrib import admin
from django.urls import path
from .views import home,product_grid
urlpatterns = [
path("home/",home,name="home"),
path("product_grid/", product_grid, name="product_grid"),
]


