from src.bingo import carton

def test_fila_con_5():
    cinco_por_fila = carton()

    #variables con la primera tupla (0) , segunda (1), tercera (2)
    mi_carton1=cinco_por_fila[0]
    mi_carton2=cinco_por_fila[1]
    mi_carton3=cinco_por_fila[2]

    y = 0

    for x in mi_carton1:
        if (x > 0):
        	y += 1 
    assert y == 5
    y = 0
    for x in mi_carton2:
        if (x > 0) :
        	y += 1 
    assert y == 5
    y = 0
    for x in mi_carton3:
        if (x > 0) :
        	y += 1 
    assert y == 5