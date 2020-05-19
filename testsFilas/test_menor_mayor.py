from src.bingo import carton

def test_uno_noventa():
    tarea6 = carton()
    for fila in range(3):
        min = 0
        max = 10
        for columna in range(9):
            if tarea6[fila][columna] != 0:
                if (tarea6[fila][columna] < min or tarea6[fila][columna] > max):
                    return False
            min += 10
            max += 10
    return True