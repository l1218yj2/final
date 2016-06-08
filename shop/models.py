from django.conf import settings
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    category = models.ForeignKey(Category, related_name='shops')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=100)
    description = models.TextField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField(null=True, blank=True)
    photo_3 = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    shop = models.ForeignKey(Shop, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
