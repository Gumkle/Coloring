from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=72)
    hex = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=120)
    file = models.ImageField(max_length=120, upload_to='images/')
    colors = models.ManyToManyField(Color, blank=True, through="ColorImage")


class ColorImage(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    percentage = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        pass
        super().save(self, *args, **kwargs)
