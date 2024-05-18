from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from .models import Category, Painting


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
    context = {'page_name': 'Landscapes'}
    return render(request, 'firstapp/portfolio/landscapes.html', context)

def japanese_koi_fish(request):
    context = {'page_name': 'Japanese Koi Fish'}
    return render(request, 'firstapp/portfolio/japanese_koi_fish.html', context)

def food(request):
    context = {'page_name': 'Food'}
    return render(request, 'firstapp/portfolio/food.html', context)

def wooden_kokeshi_dolls(request):
    context = {'page_name': 'Wooden Kokeshi Dolls'}
    return render(request, 'firstapp/portfolio/wooden_kokeshi_dolls.html', context)

def teapots(request):
    context = {'page_name': 'Teapots'}
    return render(request, 'firstapp/portfolio/teapots.html', context)


def statement(request):
    context = {
        "page_name": "statement",
    }
    return render(request, "firstapp/statement.html", context)



# The CategoryListView is a generic ListView for the Category model.
# It uses the category_list.html template.
class CategoryListView(ListView):
    model = Category
    template_name = 'firstapp/category_list.html'

# The PaintingListView is a generic ListView for the Painting model.
# It uses the painting_list.html template and filters the paintings by category name.
class PaintingListView(ListView):
    template_name = 'firstapp/painting_list.html'
    context_object_name = 'paintings'

    # The get_queryset method is overridden to filter the paintings by category name.
    def get_queryset(self):
        return Painting.objects.filter(category__name=self.kwargs['category_name'])

    # The get_context_data method is overridden to add the category name to the context.
    # This allows the category name to be used as the page name in the template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = self.kwargs['category_name']
        return context
