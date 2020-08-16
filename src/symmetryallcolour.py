from src.symmetrybwdiagonal import bwsymmetryindexdiagonal, bwsymmetryindexdiagonal2
from src.symmetrybwhorizontal import bwsymmetryindexhorizontal
from src.symmetrybwvertical import bwsymmetryindexvertical
from src.symmetrycolourdiagonal import coloursymmetryindexdiagonal, coloursymmetryindexdiagonal2
from src.symmetrycolourhorizontal import coloursymmetryindexhorizontal
from src.symmetrycolourvertical import coloursymmetryindexvertical

x = [158]

for i in x:
    num = str(i)
    filename = 'icons/'+num+'.jpg'
    indexhorizontal = coloursymmetryindexhorizontal(filename)
    indexvertical = coloursymmetryindexvertical(filename)
    indexdi1 = coloursymmetryindexdiagonal(filename)
    indexdi2 = coloursymmetryindexdiagonal2(filename)
    # index = (max(indexhorizontal, indexvertical, indexdi1, indexdi2))
    print (filename)
    print(indexvertical, indexhorizontal, indexdi1, indexdi2)
    # print (index)



    # make all the functions return the value and add it to a list and then return the max value in the list

