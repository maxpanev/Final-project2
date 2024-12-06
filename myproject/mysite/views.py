from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'flowers/home.html')

def basket(request):
    return render(request, 'flowers/basket.html')
