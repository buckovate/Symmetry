import math

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def coloursymmetryindexverticaltol(filename):
# read in image
    im = Image.open(filename)

# convert it to ndarray of 512x512 pixels
    im = np.array(im)

# split it into two halves in the middle - horizontal
    lefthalf = im[:, 0:256]
    righthalf = im[:,256:512]
    rows = lefthalf.shape[0]
    cols = lefthalf.shape[1]


    pil_img = Image.fromarray(lefthalf)
    pil_img.save('output/lefthalf.jpg')

    plt.imshow(lefthalf)

# split it into two halves in the middle - vertical
    righthalf = np.fliplr(righthalf)


# compare it
    same = 0
    for j in range(0, cols - 1):
        for k in range(0, rows - 1):
            if math.isclose(righthalf[k, j, 0], lefthalf[k, j, 0]) & math.isclose(righthalf[k, j, 1], lefthalf[k, j,1]) & math.isclose(righthalf[k, j, 2], lefthalf[k, j, 2]):
                same = same + 1

    return (same/(cols*rows))