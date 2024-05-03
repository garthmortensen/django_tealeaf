from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'firstapp/home.html', {'message': 'Hello, Mars!'})

def contact(request):
    return render(request, 'firstapp/contact.html')

def portfolio(request):
    return render(request, 'firstapp/portfolio.html')

def statement(request):
    return render(request, 'firstapp/statement.html')
