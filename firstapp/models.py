from django.db import models
from PIL import Image  # for image orientation

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# this generates the upload path for the image field
def get_upload_path(instance, filename):
    return 'paintings/{}/{}'.format(instance.category.name, filename)

# Painting model has FK to the Category model
class Painting(models.Model):
    category = models.ForeignKey(
        Category, related_name="paintings", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=get_upload_path)

    # determine if the image is portrait or landscape, and return the orientation
    # this is used to set the image dimensions in the template
    def image_orientation(self):
        image = Image.open(self.image.path)
        return 'portrait' if image.height > image.width else 'landscape'

    def __str__(self):
        return self.title
