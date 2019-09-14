from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=72)
    hex = models.CharField(max_length=7)


class Image(models.Model):
    title = models.CharField(max_length=120)
    filename = models.CharField(max_length=120)
    colors = models.ManyToManyField(Color)
