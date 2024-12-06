from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Profile
from django.http import HttpResponse


def index(request):
    return render(request, 'layoute.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('layoute')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('layoute')
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


def home(request):
    return render(request, 'home.html')

def basket(request):
    return render(request, 'basket.html')