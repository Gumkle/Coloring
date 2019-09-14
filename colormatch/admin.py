from django.contrib import admin
from .models import Color, Image


class ImageAdmin(admin.ModelAdmin):
    exclude = ('colors',)


admin.site.register(Color)
admin.site.register(Image, ImageAdmin)
