from django.urls import path
from .views import home, contact

# create a list of URL patterns
urlpatterns = [
    path("", home, name="home"),
    path('contact/', contact, name='contact'),
]
