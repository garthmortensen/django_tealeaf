from django.contrib import admin
from .models import Category, Painting


class PaintingAdmin(admin.ModelAdmin):
    # list_display is a tuple of field names to display in the admin paintings table view
    list_display = ("id", "category", "title", "description", "image_path")

    # need to define a function to get the image path
    def image_path(self, obj):
        return obj.image.name
    image_path.short_description = "Image Path"

admin.site.register(Category)
admin.site.register(Painting, PaintingAdmin)
