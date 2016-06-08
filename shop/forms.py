from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['message', 'photo']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['category', 'name', 'phone', 'location', 'description', 'photo_1', 'photo_2', 'photo_3']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['shop', 'message', 'photo']
