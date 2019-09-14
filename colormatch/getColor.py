from colormatch.importColors import get_colors
import math


def get_color(c):
    dist = []
    for color in get_colors():
        d = math.sqrt(
            (c[0] - color[0][0]) ** 2 + (c[1] - color[0][1]) ** 2 + (c[2] - color[0][2]) ** 2)
        dist.append((color, d))
    min_of_d = min(dist)
    dist.sort(key=get_val)
    colors = []
    for i in range(3):
        colors.append(dist[i][0])
    return colors


def get_val(val):
    return val[1]
