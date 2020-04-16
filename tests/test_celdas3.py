from src.bingo import carton

def test3():
    tarea3 = carton()
    mi_carton1=tarea3[0]
    mi_carton2=tarea3[1]
    mi_carton3=tarea3[2]
    i=0
    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if (x==1 or y==1 or z==1):
            i += 1

    assert i == 9
