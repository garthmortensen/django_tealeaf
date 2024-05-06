from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        "page_name": "home",
        "message": "Hello, Mars!",
    }
    return render(request, "firstapp/home.html", context)


def contact(request):
    context = {
        "page_name": "contact",
    }
    return render(request, "firstapp/contact.html", context)


def portfolio(request):
    context = {
        "page_name": "portfolio",
    }
    return render(request, "firstapp/portfolio.html", context)


def statement(request):
    context = {
        "page_name": "statement",
    }
    return render(request, "firstapp/statement.html", context)
