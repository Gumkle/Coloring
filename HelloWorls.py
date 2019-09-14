import os
import time

import math
from PIL import Image


def get_key(val):
    return val[0]


def get_color(c):
    dist = []
    for color in get_colors():
        d = math.sqrt((c[1][0] - color[0][0]) ** 2 + (c[1][1] - color[0][1]) ** 2 + (c[1][2] - color[0][2]) ** 2)
        dist.append(d)
    min_of_d = min(dist)
    index = dist.index(min_of_d)
    return get_colors()[index][1]


def find_image_by_color(color_name):
    names = os.listdir("images")
    ret_names = []
    for name in names:
        colors = get_image_colors(name)
        for i in range(3):
            if colors[i][1] == color_name:
                ret_names.append(name)

    return ret_names


def get_counts(found_colors, pixels):
    counts = []
    s = 0
    for i in get_colors():
        s += found_colors.count(i[1])
        counts.append((round(found_colors.count(i[1]) / pixels, 2), i[1]))
    return counts


def get_image_colors(image):
    print(image)
    im = Image.open("images\\" + image)
    im = im.convert('RGB')
    width, height = im.size
    im = im.resize((int(width / 4), int(height / 4)))
    width, height = im.size
    pixels = width * height

    colors = im.getcolors(maxcolors=1000000)
    colors_found = []
    for c in colors:
        color = get_color(c)
        for i in range(c[0]):
            colors_found.append(color)
    colors_found = get_counts(colors_found, pixels)
    colors_found.sort(key=get_key, reverse=True)
    return colors_found


if __name__ == '__main__':
    files = os.listdir("images")
    print(get_image_colors(files[0]))

    start_time = time.time()
    a = find_image_by_color("teal")
    elapsed_time = time.time() - start_time
    print("Time:", elapsed_time)
    print(len(a))
