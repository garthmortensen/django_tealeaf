from django.urls import path
from .views import home

# create a list of URL patterns
urlpatterns = [
    path("", home, name="home"),
]
