from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Shop, Category, Review

def index(request):
    pass

def category_new(request):
    pass

def category_edit(request, pk):
    pass

def category_detail(request, pk):
    pass

def shop_new(request):
    pass

def shop_edit(request, pk):
    pass

def shop_detail(request, pk):
    pass

def review_new(reqeust):
    pass

def review_edit(request):
    pass

def category_delete(request, pk):
    pass

def shop_delete(request, pk):
    pass

def review_delete(request, pk):
    pass
