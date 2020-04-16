from src.bingo import carton

def test2():
    tarea2 = carton()
    i = 0
    for fila in tarea2:
        for celda in fila:
            i += celda

    assert i <= 15
