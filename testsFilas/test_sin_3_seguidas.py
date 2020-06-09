from src.bingo import carton

def test_sin_3_celdas_ocupadas():
    mi_carton = carton()
    for fila in mi_carton:
        i = 0
        for celda in fila:
            if celda == 0:
                i = 0
            else:
                i += 1
            if i == 3:
                assert False
    assert True

def test_sin_3_celdas_vacias():
    mi_carton = carton()
    for fila in mi_carton:
        i = 0
        for celda in fila:
            if celda != 0:
                i = 0
            else:
                i += 1
            if i == 3:
                assert False
    assert True