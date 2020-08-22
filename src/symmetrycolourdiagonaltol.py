import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import math

def coloursymmetryindexdiagonaltol(filename):
# read in image

    im = Image.open(filename)

# convert it to greyscale

# img_grey.show()

# convert it to ndarray of 512x512 pixels
    im = np.array(im)
    # print(im.shape)

# # split it into two halves in the middle - vertical
#     lefthalf = im[:, 0:256]
#     righthalf = im[:,256:512]
#     rows = lefthalf.shape[0]
#     cols = lefthalf.shape[1]
    # print(rows)
    # print(cols)

    # pil_img = Image.fromarray(lefthalf)
    # pil_img.save('output/lefthalf.jpg')
    #
    # plt.imshow(lefthalf)

# split it into two halves in the middle - vertical

# flip it
#     pil_img = Image.fromarray(righthalf)
#     im_mirror = ImageOps.mirror(pil_img)
#     im_mirror.save('output/flipped.jpg')
#     righthalf = np.fliplr(righthalf)


# compare it
    same = 0
    comparison = 0
    for y in range(1, 512):
        for x in range(1, y):
            if math.isclose(im[y, x, 0], im[-x, -y, 0]) & math.isclose(im[y, x, 1], im[-x, -y, 1]) & math.isclose(im[y, x, 2], im[-x, -y, 2]):
                same = same + 1
            comparison = comparison + 1


    # print(same)
    # print (same/((cols*rows)))
    return (same/(comparison))

def coloursymmetryindexdiagonal2tol(filename):
# read in image

    im = Image.open(filename)

# convert it to greyscale

# img_grey.show()

# convert it to ndarray of 512x512 pixels
    im = np.array(im)
    # print(im.shape)

# # split it into two halves in the middle - vertical
#     lefthalf = im[:, 0:256]
#     righthalf = im[:,256:512]
#     rows = lefthalf.shape[0]
#     cols = lefthalf.shape[1]
    # print(rows)
    # print(cols)

    # pil_img = Image.fromarray(lefthalf)
    # pil_img.save('output/lefthalf.jpg')
    #
    # plt.imshow(lefthalf)

# split it into two halves in the middle - vertical

# flip it
#     pil_img = Image.fromarray(righthalf)
#     im_mirror = ImageOps.mirror(pil_img)
#     im_mirror.save('output/flipped.jpg')
#     righthalf = np.fliplr(righthalf)


# compare it


    same1 = 0
    comparison1 = 0
    for y in range(1, 512):
        for x in range(1, y):
            if math.isclose(im[y, x, 0], im[x, y, 0]) & math.isclose(im[y, x, 1],im[x, y, 1]) & math.isclose(im[y, x, 2], im[x, y, 2]):
                same1 = same1 + 1
            comparison1 = comparison1 + 1


    # print(same)
    # print (same/((cols*rows)))
    return (same1/(comparison1))
