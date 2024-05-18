from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Painting(models.Model):
    category = models.ForeignKey(Category, related_name='paintings', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='paintings/')

    def __str__(self):
        return self.title
