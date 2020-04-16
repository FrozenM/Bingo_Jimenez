from src.bingo import carton

def test4():
    tarea4 = carton()
    mi_carton1=tarea4[0]
    mi_carton2=tarea4[1]
    mi_carton3=tarea4[2]
    i=0
    j=0
    k=0
    for x in mi_carton1:
        i += x
    for z in mi_carton2:
        j += z
    for y in mi_carton3:
        k += y
    assert i > 0
    assert j > 0
    assert k > 0
