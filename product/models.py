import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def get_file_path(instance, filename):
    return f'{settings.MEDIA_ROOT}/product/{instance.id}/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=128)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to=get_file_path)
    price = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment
    