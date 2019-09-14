from django.shortcuts import render
from django.http import HttpResponse
from .getColor import get_color
from colormatch.models import ColorImage


def index(request):
    return render(request, 'colormatch/index.html', context={})


def search(request):
    inputColor = request.POST['color'].lstrip('#')
    inputColor = tuple(int(inputColor[i:i+2], 16) for i in (0, 2, 4))
    similarColors = get_color(inputColor)
    
    return HttpResponse(similarColors)
