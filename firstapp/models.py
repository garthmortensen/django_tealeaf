from django.db import models


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

    def __str__(self):
        return self.title
