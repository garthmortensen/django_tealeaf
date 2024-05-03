from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'firstapp/home.html', {'message': 'Hello from Django!'})
