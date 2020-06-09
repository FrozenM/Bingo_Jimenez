from src.bingo import carton

def test_columna_sola():
    columna_so = carton()

    #variables con la primera tupla (0) , segunda (1), tercera (2)
    mi_carton1=columna_so[0]
    mi_carton2=columna_so[1]
    mi_carton3=columna_so[2]

    #Variable para contar si hay alguna celda ocupada en la columna
    i=0

    #El zip logra hacer una lista de tuplas y el x y z representan al primero, segundo y tercero de la tupla respectivamente
    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if ((x>=1 and y==0 and z==0) or (x==0 and y>=1 and z==0) or (x==0 and y==0 and z>=1)):
            i += 1

    assert i == 3