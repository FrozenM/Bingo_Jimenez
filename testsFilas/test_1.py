from src import bingo

mi_carton = [
    [0,5,0,5,5,5,0,5,5],
    [1,4,0,0,0,0,0,0,0],
    [0,3,0,0,0,2,0,0,100]
]

celdas_sean_15 = bingo.celdas_sean_15(mi_carton)

def test_15_celdas_ocupadas():
    assert celdas_sean_15 != 15

def test_fila_con_5():
    assert (bingo.fila_con_5(mi_carton[0]) != 5
    and bingo.fila_con_5(mi_carton[1]) != 5
    and bingo.fila_con_5(mi_carton[2]) != 5)

def test_no_haya_columnas_vacias():
    assert not(bingo.no_haya_columnas_vacias(mi_carton))

def test_no_haya_columna_llena_o_filas_vacias():
    assert not(bingo.no_haya_columna_llena(mi_carton) and bingo.no_haya_filas_vacias(mi_carton))

def test_sin_3_celdas_ocupadas():
    assert not(bingo.sin_3_celdas_ocupadas(mi_carton))

def test_sin_3_celdas_vacias():
    assert not(bingo.sin_3_celdas_vacias(mi_carton))

def test_columna_sola():
    assert bingo.columna_sola(mi_carton) != 3

def test_uno_noventa():
    assert not(bingo.uno_noventa(mi_carton))

def test_mayores_a_la_derecha():
    assert not(bingo.mayores_a_la_derecha(mi_carton))

def test_columna_may_men():
    assert not(bingo.columna_may_men(mi_carton))

def test_no_haya_numero_repetido():
    assert not(bingo.no_haya_numero_repetido(mi_carton))
