from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=72)
    hex = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=120)
    file = models.FileField(max_length=120)
    colors = models.ManyToManyField(Color, blank=True)

    def __str__(self):
        return self.title
