from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('about', TemplateView.as_view(template_name="product/about.html")),
    path('category', views.CategoryList.as_view()),
    # path('products', views.ProductList.as_view()),
    # path('products/<str:category_name>', views.CategoryBookList.as_view()),
    # path('product/<str:product_id>', views.DetailView.as_view(), name='product-detail'),
]
