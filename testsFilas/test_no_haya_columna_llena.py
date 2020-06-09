from src.bingo import carton

def test_no_haya_columna_llena():
    prueba = carton()

    #variables con la primera tupla (0) , segunda (1), tercera (2)
    mi_carton1=prueba[0]
    mi_carton2=prueba[1]
    mi_carton3=prueba[2]

    #El zip logra hacer una lista de tuplas y el x y z representan al primero, segundo y tercero de la tupla respectivamente
    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if (x>=1 and y>=1 and z>=1):
            assert False

    assert True