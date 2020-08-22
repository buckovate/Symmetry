from src.symmetrycolourdiagonal import coloursymmetryindexdiagonal, coloursymmetryindexdiagonal2
from src.symmetrycolourhorizontal import coloursymmetryindexhorizontal
from src.symmetrycolourvertical import coloursymmetryindexvertical

x = [252, 78]

for i in x:
    num = str(i)
    filename = 'icons/'+num+'.jpg'
    indexhorizontal = coloursymmetryindexhorizontal(filename)
    # indexvertical = coloursymmetryindexvertical(filename)
    # indexdi1 = coloursymmetryindexdiagonal(filename)
    # indexdi2 = coloursymmetryindexdiagonal2(filename)
    # index = (max(indexhorizontal, indexvertical, indexdi1, indexdi2))
    indexsym = coloursymmetryindexdiagonal2(filename)
    indexsym2 = coloursymmetryindexdiagonal(filename)
    # print (filename)
    print(indexhorizontal)
    # print (index)
    print(indexsym, indexsym2)




