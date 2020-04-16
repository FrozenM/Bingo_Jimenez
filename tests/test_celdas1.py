from src.bingo import carton

def test1():
    tarea1 = carton()
    i = 0
    for fila in tarea1:
        for celda in fila:
            i += celda

    assert i >= 15
