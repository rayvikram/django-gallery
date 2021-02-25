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
    date_hierarchy = 'updated_at'
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    search_fields = ['name']

admin.site.site_header = "Gallery Admin"
admin.site.site_title = "Gallery Admin"