from django.urls import path
from .views import (
    home,
    contact,
    landscapes,
    japanese_koi_fish,
    food,
    wooden_kokeshi_dolls,
    teapots,
    statement,
)

from .views import CategoryListView, PaintingListView

from django.conf import settings
from django.conf.urls.static import static

# create a list of URL patterns
urlpatterns = [
    path(route="", view=home, name="home"),
    path(route="contact/", view=contact, name="contact"),
    path(route="landscapes/", view=landscapes, name="landscapes"),
    path(route="japanese_koi_fish/", view=japanese_koi_fish, name="japanese_koi_fish"),
    path(route="food/", view=food, name="food"),
    path(
        route="wooden_kokeshi_dolls/",
        view=wooden_kokeshi_dolls,
        name="wooden_kokeshi_dolls",
    ),
    path(route="teapots/", view=teapots, name="teapots"),
    path(route="statement/", view=statement, name="statement"),
    path(route="", view=CategoryListView.as_view(), name="category-list"),
    path(
        route="category/<str:category_name>/",
        view=PaintingListView.as_view(),
        name="painting-list",
    ),
    # tells Django to serve media files at MEDIA_URL from MEDIA_ROOT when DEBUG is True.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
