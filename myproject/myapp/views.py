from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Profile, Product, Basket, BasketItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return render(request, 'layoute.html')

def home(request):
    return render(request, 'home.html')


@login_required
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket_item, item_created = BasketItem.objects.get_or_create(basket=basket, product=product)

    if not item_created:
        basket_item.quantity += 1
        basket_item.save()

    return redirect('basket')


@login_required
def basket(request):
    basket, created = Basket.objects.get_or_create(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in basket.items.all())
    return render(request, 'basket.html', {'basket': basket, 'total_price': total_price})


@login_required
def remove_from_basket(request, item_id):
    basket_item = get_object_or_404(BasketItem, id=item_id, basket__user=request.user)
    basket_item.delete()
    return redirect('basket')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')  # Измените 'layoute' на 'home'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Измените 'layoute' на 'home'
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('layoute')

def layoute(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user=request.user)
    return render(request, 'layoute.html', {'profile': profile})