from .models import Category

# To make a variable available to all views, use Django's context processors.
# Context processor = function that takes the request object, returns a dict
# this dict is added to the context
def website_name(request):
    return {"website_name": "TL Gallery",}

# this is for dynamically populating the navigation bar with categories
def categories(request):
    return {'categories': Category.objects.all()}
