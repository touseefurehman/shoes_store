
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from products import urls
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("products.urls")),  # Include the products app urls
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
