from src.symmetrycolourdiagonal import coloursymmetryindexdiagonal
from src.symmetrycolourdiagonaltol import coloursymmetryindexdiagonal2tol, coloursymmetryindexdiagonaltol
from src.symmetrycolourhorizontaltolerance import coloursymmetryindexhorizontaltol
from src.symmetrycolourverticaltol import coloursymmetryindexverticaltol

x = [252, 78, 158, 20, 184, 242, 211, 205, 239]

for i in x:
    num = str(i)
    filename = 'icons/'+num+'.jpg'
    indexhorizontal = coloursymmetryindexhorizontaltol(filename)
    indexvertical = coloursymmetryindexverticaltol(filename)
    indexdi1 = coloursymmetryindexdiagonaltol(filename)
    indexdi2 = coloursymmetryindexdiagonal2tol(filename)
    index = (max(indexhorizontal, indexdi1, indexdi2))
    # indexsym = coloursymmetryindexdiagonal2tol(filename)
    # indexsym2 = coloursymmetryindexdiagonaltol(filename)
    # indexsym = coloursymmetryindexdiagonal2tol(filename)
    # indexsym2 = coloursymmetryindexdiagonaltol(filename)
    # print (filename)
    print( indexhorizontal,indexvertical, indexdi1, indexdi2)
    # print (index)
    # print(indexsym, indexsym2)




