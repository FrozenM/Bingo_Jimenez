from src.bingo import carton

def test_columna_may_men():
    tarea6 = carton()

    mi_carton1=tarea6[0]
    mi_carton2=tarea6[1]
    mi_carton3=tarea6[2]

    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if (x > y and y != 0):
            assert False
        if (y > z and z != 0):
            assert False
        if (x > z and z != 0):
            assert False
    assert True