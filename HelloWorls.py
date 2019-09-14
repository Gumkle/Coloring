import os

import math
from PIL import Image


def get_key(val):
    return val[0]


def get_color(c):
    colors = get_colors()
    dist = []
    for color in colors:
        d = math.sqrt((c[1][0] - color[0][0]) ** 2 + (c[1][1] - color[0][1]) ** 2 + (c[1][2] - color[0][2]) ** 2)
        dist.append(d)
    min_of_d = min(dist)
    index = dist.index(min_of_d)
    return colors[index][1]


def get_colors():
    return [
        [(255, 255, 255), "white"],
        [(192, 192, 192), "silver"],
        [(128, 128, 128), "gray"],
        [(0, 0, 0), "black"],
        [(255, 0, 0), "red"],
        [(128, 0, 0), "maroon"],
        [(255, 255, 0), "yellow"],
        [(0, 0, 0), "olive"],
        [(0, 255, 0), "lime"],
        [(0, 128, 0), "green"],
        [(0, 255, 255), "aqua"],
        [(0, 128, 128), "teal"],
        [(0, 0, 255), "blue"],
        [(0, 0, 128), "navy"],
        [(255, 0, 255), "fuchsia"],
        [(128, 0, 128), "purple"]
    ]


def get_counts(found_colors, pixels):
    counts = []
    s = 0
    for i in get_colors():
        s += found_colors.count(i[1])
        counts.append((round(found_colors.count(i[1]) / pixels, 2), i[1]))
    return counts


if __name__ == '__main__':
    files = os.listdir("images")

    im = Image.open("images\\" + files[0])
    im = im.convert('RGB')
    width, height = im.size
    pixels = width * height
    print(pixels)
    colors = im.getcolors(maxcolors=1000000)
    colors_found = []
    for c in colors:
        color = get_color(c)
        for i in range(c[0]):
            colors_found.append(color)
    colors_found = get_counts(colors_found, pixels)
    colors_found.sort(key=get_key, reverse=True)
    print(colors_found)
