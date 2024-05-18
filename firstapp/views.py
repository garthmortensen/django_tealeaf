from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        "page_name": "home",
        # "message": "Hello, user!",
    }
    return render(request, "firstapp/home.html", context)


def contact(request):
    context = {
        "page_name": "contact",
    }
    return render(request, "firstapp/contact.html", context)


def landscapes(request):
    context = {'title': 'Landscapes'}
    return render(request, 'firstapp/portfolio/landscapes.html', context)

def japanese_koi_fish(request):
    context = {'title': 'Japanese Koi Fish'}
    return render(request, 'firstapp/portfolio/japanese_koi_fish.html', context)

def food(request):
    context = {'title': 'Food'}
    return render(request, 'firstapp/portfolio/food.html', context)

def wooden_kokeshi_dolls(request):
    context = {'title': 'Wooden Kokeshi Dolls'}
    return render(request, 'firstapp/portfolio/wooden_kokeshi_dolls.html', context)

def teapots(request):
    context = {'title': 'Teapots'}
    return render(request, 'firstapp/portfolio/teapots.html', context)


def statement(request):
    context = {
        "page_name": "statement",
    }
    return render(request, "firstapp/statement.html", context)
