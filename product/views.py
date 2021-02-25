from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Product, Category


class HomeView(View):
    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {"data": Product.objects.all()}
        return render(request, 'product/home.html', context )

class CategoryList(ListView):
    template_name = 'product/category.html'

    def get_queryset(self):
        self.category = Category.objects.all()
        print(self.category)
        return self.category
