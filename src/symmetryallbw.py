from src.symmetrybwdiagonal import bwsymmetryindexdiagonal
from src.symmetrybwhorizontal import bwsymmetryindexhorizontal
from src.symmetrybwvertical import bwsymmetryindexvertical

for i in range (1, 260):
    num = str(i)
    filename = 'icons/'+num+'.jpg'
    indexhorizontal = bwsymmetryindexhorizontal(filename)
    indexvertical = bwsymmetryindexvertical(filename)
    index = (max( indexhorizontal, indexvertical))
    indexdi = bwsymmetryindexdiagonal(filename)
    index = (max(indexhorizontal, indexvertical, indexdi))
    print(i)
    print (index)
    print (indexdi)

    # make all the functions return the value and add it to a list and then return the max value in the list

