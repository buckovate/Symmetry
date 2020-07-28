import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def bwsymmetryindexhorizontal(filename):
# read in image

    im = Image.open(filename)

# convert it to greyscale
    img_grey = im.convert("L")
# img_grey.show()

# convert it to ndarray of 512x512 pixels
    im = np.array(img_grey)
    # print(im.shape)

# split it into two halves in the middle - horizontal
    lefthalf = im[0:256, :]
    righthalf = im[256:512, :]
    rows = lefthalf.shape[0]
    cols = lefthalf.shape[1]

    pil_img = Image.fromarray(lefthalf)
    pil_img.save('output/lefthalf.jpg')

    plt.imshow(lefthalf)

# split it into two halves in the middle - vertical

# flip it
#     pil_img = Image.fromarray(righthalf)
#     im_mirror = pil_img.rotate(180)
#     im_mirror.save('output/flipped.jpg')
    righthalf = np.flipud(righthalf)
    pil_img = Image.fromarray(righthalf)
#     im_mirror = pil_img.rotate(180)
    pil_img.save('output/flipped.jpg')


# compare it
    same = 0
    for j in range(0, cols - 1):
        for k in range(0, rows - 1):
            if (righthalf[k, j] == lefthalf[k, j]):
                same = same + 1

    # print(filename)
    # print (same/((512*512)/2))
    return same/((cols*rows))


















