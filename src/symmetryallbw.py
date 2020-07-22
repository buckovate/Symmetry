import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

from src.symmetrybwhorizontal import bwsymmetryindexhorizontal
from src.symmetrybwvertical import bwsymmetryindexvertical

for i in range (1, 260):
    num = str(i)
    filename = 'icons/'+num+'.jpg'
    bwsymmetryindexhorizontal(filename)
    bwsymmetryindexvertical(filename)

    # make all the functions return the value and add it to a list and then return the max value in the list

