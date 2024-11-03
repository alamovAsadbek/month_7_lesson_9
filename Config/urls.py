from django.contrib import admin
from django.urls import path

from app_product import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', product_views.ProductViewForUser.as_view(), name='product')
]
