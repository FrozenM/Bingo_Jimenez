from src.bingo import carton

def test7():
	tarea7 = carton()
	numeros = set()
	for fila in tarea7:
		for celda in fila:
			if (celda in numeros) and celda != 0:
				assert False
			numeros.add(celda)
	assert True

