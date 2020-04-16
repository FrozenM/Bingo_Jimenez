from src.bingo import carton

def test4():
    tarea4 = carton()
    
    #Agrego variables para que tengan las tuplas correspondientes de carton()
    mi_carton1=tarea4[0]
    mi_carton2=tarea4[1]
    mi_carton3=tarea4[2]

    #Contadores para saber si hay o no 1 en las filas
    a=0
    j=0
    k=0

    #Los fors recorren la tupla buscando almenos 1 celda ocupada de la fila
    for x in mi_carton1:
        a += x
    for z in mi_carton2:
        j += z
    for y in mi_carton3:
        k += y
    assert a > 0
    assert j > 0
    assert k > 0
