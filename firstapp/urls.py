from django.urls import path
from .views import home, contact, landscapes, japanese_koi_fish, food, wooden_kokeshi_dolls, teapots, statement

# create a list of URL patterns
urlpatterns = [
    path(route="", view=home, name="home"),
    path(route='contact/', view=contact, name='contact'),
    path(route='landscapes/', view=landscapes, name='landscapes'),
    path(route='japanese_koi_fish/', view=japanese_koi_fish, name='japanese_koi_fish'),
    path(route='food/', view=food, name='food'),
    path(route='wooden_kokeshi_dolls/', view=wooden_kokeshi_dolls, name='wooden_kokeshi_dolls'),
    path(route='teapots/', view=teapots, name='teapots'),
    path(route='statement/', view=statement, name='statement'),
]
