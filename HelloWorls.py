import os

from PIL import Image


def get_key(val):
    return val[0]


if __name__ == '__main__':
    files = os.listdir("images")

    im = Image.open("images\\" + files[0])
    im = im.convert('RGB')

    colors = im.getcolors(maxcolors=1000000)
    colors.sort(key=get_key, reverse=True)
    for c in colors:
        print(c)
