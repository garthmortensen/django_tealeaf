from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home,
    contact,
    statement,
)

# content management
from .views import CategoryListView, PaintingListView

# create a list of URL patterns
urlpatterns = [
    # Home: http://127.0.0.1:8000/
    path(route="", view=home, name="home"),
    # Home: http://127.0.0.1:8000/statement
    path(route="statement/", view=statement, name="statement"),
    # Home: http://127.0.0.1:8000/contact
    path(route="contact/", view=contact, name="contact"),
    # Home: http://127.0.0.1:8000/
    path(route="", view=CategoryListView.as_view(), name="category-list"),
    # http://127.0.0.1:8000/category/Landscapes/
    path(
        route="category/<str:category_name>/",
        view=PaintingListView.as_view(),
        name="painting-list",
    ),
    # tells Django to serve media files at MEDIA_URL from MEDIA_ROOT when DEBUG is True.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
