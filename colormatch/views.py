from django.shortcuts import render
from django.http import HttpResponse
from .getColor import get_color
from colormatch.models import ColorImage, Color, Image


def index(request):
    return render(request, 'colormatch/index.html', context={})


def search(request):
    inputColor = request.POST['color'].lstrip('#')
    inputColor = tuple(int(inputColor[i:i+2], 16) for i in (0, 2, 4))
    similarColorsOld = get_color(inputColor)
    similarColors = []
    for color in similarColorsOld:
        similarColors.append(Color.objects.filter(name=color[1])[0])

    colorsImages = ColorImage.objects.filter(color__in=similarColors, percentage__gt=0)
    totalColorImagesValues = []
    for colorImage in colorsImages:
        totalColorImagesValues.append([colorImage.image_id, colorImage.percentage])
        #totalColorImagesValues[str(colorImage.image_id)] += colorImage.percentage

    tab = []
    for c in totalColorImagesValues:
        ind = inde(tab, c[0])
        if ind >= 0:
            tab[ind][1] += c[1]
        else:
            tab.append([c[0], c[1]])

    tab.sort(reverse=True, key=genkey)

    images = []

    for element in tab[:15]:
        images.append(Image.objects.filter(id=element[0])[0].file)

    return render(request, 'colormatch/index.html', {'images': images})

def inde(cim, id):
    for i in range(len(cim)):
        if cim[i][0] == id:
            return i
    return -1

def genkey(val):
    return val[1]