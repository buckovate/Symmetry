import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def bwsymmetryindexdiagonal(filename):
# read in image

    im = Image.open(filename)

# convert it to greyscale
    img_grey = im.convert("L")

# convert it to ndarray of 512x512 pixels
    im = np.array(img_grey)
    # print(im.shape)

# compare it
    same1 = 0
    comparison1 = 0
    for y in range(1, 512):
        for x in range(1, y):
            if (im[y, x] == im[x, y]):
                same1 = same1 + 1
            comparison1 = comparison1 + 1


    # print(same)
    # print (same/((cols*rows)))
    return (same1/(comparison1))


def bwsymmetryindexdiagonal2(filename):
# read in image
    im = Image.open(filename)

# convert it to greyscale
    img_grey = im.convert("L")

# convert it to ndarray of 512x512 pixels
    im = np.array(img_grey)

# compare it
    same = 0
    comparison = 0
    for y in range(1, 512):
        for x in range(1, y):
            if (im[y, x] == im[-y, -x]):
                same = same + 1
            comparison = comparison + 1


    # print(same)
    # print (same/((cols*rows)))
    return (same/((comparison)))
