from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['category', 'name', 'phone', 'location', 'description', 'photo_1', 'photo_2', 'photo_3']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['message', 'photo']
