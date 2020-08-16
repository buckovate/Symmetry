from src.symmetrybwdiagonal import bwsymmetryindexdiagonal, bwsymmetryindexdiagonal2
from src.symmetrybwhorizontal import bwsymmetryindexhorizontal
from src.symmetrybwvertical import bwsymmetryindexvertical

for i in range (1, 260):
    num = str(i)
    filename = 'icons/'+num+'.jpg'
    indexhorizontal = bwsymmetryindexhorizontal(filename)
    indexvertical = bwsymmetryindexvertical(filename)
    # index = (max( indexhorizontal, indexvertical))
    indexdi1 = bwsymmetryindexdiagonal(filename)
    indexdi2 = bwsymmetryindexdiagonal2(filename)
    # index = (max(indexhorizontal, indexvertical, indexdi1, indexdi2))
    print (filename)
    print(indexhorizontal, indexvertical, indexdi1, indexdi2)
    # print (index)



    # make all the functions return the value and add it to a list and then return the max value in the list

