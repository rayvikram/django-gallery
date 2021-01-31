from django.contrib import admin
from .models import Comment, Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

