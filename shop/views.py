from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Shop, Category, Review
from .forms import ShopForm, CategoryForm, ReviewForm


def index(request):
    category_list = Category.objects.all()
    review_list = Review.objects.all().order_by('-created_at')
    return render(request, 'index.html',{
        'category_list':category_list,
        'review_list':review_list,
    })

def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, 'you made a new category.')
            return redirect('shop:category_detail', category.pk)
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {
        'form':form,
    })

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, 'you edited a cantegory.')
            return redirect('shop:category_detail', pk)

    else:
        form = CategoryForm(instance = category)
    return render(request, 'category_form.html', {
        'form':form,
    })
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {
        'category':category,
    })

@login_required
def shop_new(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.sae(commit=False)
            shop.user = request.user
            shop.save()
            messages.success('you made a new shop.')
            return redirect('shop:shop_detail', shop.pk)
    else:
        form = ShopForm()
    return render(request, 'shop_form.html', {
        'form':form,
    })

@login_required
def shop_edit(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if reqeust.method == 'POST':
        form = ShopForm(request.POST, instance = shop)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.save()
            messages.success(request, 'you edited a shop')
            return redirect('shop:shop_detail', pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop_form.html', {
        'form':form,
    })

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shop_detail.html',{
        'shop':shop,
    })

@login_required
def review_new(request, shop_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            messages.succes(reqeust, 'you make a new review')
            return redirect('shop:shop_detail', shop_pk)
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {
        'form':form,
    })

@login_required
def review_edit(request, shop_pk ,pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk = shop_pk)
            review.upser = request.user
            messages.success(request, 'you edited a review')
            return redirct('shop:shop_detail',shop_pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review_form.html',{
        'form':form,
    })

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('shop:index')

def shop_delete(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    shop.delete()
    return redirect('shop:index')

def review_delete(request, shop_pk, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('shop:shop_detail', shop_pk)
