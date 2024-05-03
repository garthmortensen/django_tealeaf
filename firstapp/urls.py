from django.urls import path
from .views import home, contact, portfolio, statement

# create a list of URL patterns
urlpatterns = [
    path("", home, name="home"),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('statement/', statement, name='statement'),
]
