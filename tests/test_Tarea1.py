from src.bingo import carton

#Me fijo que la cantidad de celdas no sea mas que 15
def test1():
    tarea1 = carton()
    i = 0
    for fila in tarea1:
        for celda in fila:
            i += celda

    assert i >= 15

#Me fijo que la cantidad de celdas no sea menos que 15

def test2():
    tarea2 = carton()
    i = 0
    for fila in tarea2:
        for celda in fila:
            i += celda

    assert i <= 15

#Me fijo que haya almenos una celda ocupada por columna

def test3():
    tarea3 = carton()

    #variables con la primera tupla (0) , segunda (1), tercera (2)
    mi_carton1=tarea3[0]
    mi_carton2=tarea3[1]
    mi_carton3=tarea3[2]

    #Variable para contar si hay alguna celda ocupada en la columna
    i=0

    #El zip logra hacer una lista de tuplas y el x y z representan al primero, segundo y tercero de la tupla respectivamente
    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if (x==1 or y==1 or z==1):
            i += 1

    assert i == 9
