from src.bingo import carton

def test_uno_noventa():
    tarea5 = carton()
    mi_carton1=tarea5[0]
    mi_carton2=tarea5[1]
    mi_carton3=tarea5[2]
    for x in mi_carton1:
        assert x >= 0 and x <= 90
    for x in mi_carton2:
        assert x >= 0 and x <= 90
    for x in mi_carton3:
        assert x >= 0 and x <= 90