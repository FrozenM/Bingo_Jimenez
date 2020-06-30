import random
import math

#Valida que haya 15 y solo 15 celdas ocupadas 

def celdas_sean_15(mi_carton):
    i = 0
    for fila in mi_carton:
        for celda in fila:
            if celda > 0:
                i += 1
    return i

#Valida que haya 5 y solo 5 celdas ocupadas porfila

def fila_con_5(mi_carton):

    y = 0

    for x in mi_carton:
        if (x > 0):
          y += 1 
    return y

#Valida que no haya ninguna columna (la misma celda de las tres filas) vacia, ejemplo 0 0 0.

def no_haya_columnas_vacias(mi_carton):

    mi_carton1=mi_carton[0]
    mi_carton2=mi_carton[1]
    mi_carton3=mi_carton[2]

    i=0

    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if (x>=1 or y>=1 or z>=1):
            i += 1
    if(i==9):
      return True
    else:
      return False

#Valida que no haya ninguna fila vacia

def no_haya_filas_vacias(mi_carton):
    
    mi_carton1=mi_carton[0]
    mi_carton2=mi_carton[1]
    mi_carton3=mi_carton[2]

    a=0
    j=0
    k=0

    for x in mi_carton1:
        a += x
    for z in mi_carton2:
        j += z
    for y in mi_carton3:
        k += y
    
    if (a>0 and j>0 and k>0):
      return True
    else:
      return False

#Valida que los numeros varien entre 1 y 90

def uno_noventa(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if not(celda >= 0 and celda <= 90):
                return False
    return True

#Valida que los numeros vayan de menor a mayor (por fila)

def mayores_a_la_derecha(mi_carton):
    x = 0
    y = 9
    for columna in range(9):
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                if not(x <= mi_carton[fila][columna] <= y):
                    return False
        x += 10
        y += 10
        if y == 89:
            y = 90
    return True

#Valida que los numeros vayan de menor a mayor por columna

def columna_may_men(mi_carton):

    mi_carton1=mi_carton[0]
    mi_carton2=mi_carton[1]
    mi_carton3=mi_carton[2]

    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if (x > y and y != 0):
            return False
        if (y > z and z != 0):
            return False
        if (x > z and z != 0):
            return False
    return True

#Valida que no haya numeros repetidos

def no_haya_numero_repetido(mi_carton):
  numeros = set()
  for fila in mi_carton:
    for celda in fila:
      if (celda in numeros) and celda != 0:
        return False
      numeros.add(celda)
  return True

#Valida que no haya ninguna columna con las 3 celdas ocupadas

def no_haya_columna_llena(mi_carton):

    mi_carton1=mi_carton[0]
    mi_carton2=mi_carton[1]
    mi_carton3=mi_carton[2]

    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if (x>=1 and y>=1 and z>=1):
            return False
    return True

#Valida que no haya 3 celdas ocupadas consecutivamente

def sin_3_celdas_ocupadas(mi_carton):
    for fila in mi_carton:
        i = 0
        for celda in fila:
            if celda == 0:
                i = 0
            else:
                i += 1
            if i == 3:
                return False
    return True

#Valida que no haya 3 celdas vacias consecutivamente

def sin_3_celdas_vacias(mi_carton):
    for fila in mi_carton:
        i = 0
        for celda in fila:
            if celda != 0:
                i = 0
            else:
                i += 1
            if i == 3:
                return False
    return True

#Valida que haya 3 y solo 3 columnas en donda haya solo 1 celda ocupada

def columna_sola(mi_carton):

    mi_carton1=mi_carton[0]
    mi_carton2=mi_carton[1]
    mi_carton3=mi_carton[2]

    i=0

    for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
        if ((x>=1 and y==0 and z==0) or (x==0 and y>=1 and z==0) or (x==0 and y==0 and z>=1)):
            i += 1

    return i


def intentoCarton():
    contador = 0

    carton = [
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while (numerosCarton < 15):
      contador = contador + 1
      if (contador == 50):
        return intentoCarton()

      numero = random.randint(1, 90)

      columna = math.floor (numero / 10)
      if (columna == 9):
        columna = 8

      huecos = 0

      for i in range (3):
        if (carton[i][columna] == 0):
          huecos = huecos + 1
        
        if (carton[i][columna] == numero):
          huecos = 0
          break
      if (huecos < 2):
        continue

      fila = 0
      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
            huecos = huecos + 1

        if (huecos < 5 or carton[fila][columna] != 0):
          fila = fila + 1
        else:
          break

      if (fila == 3):
        continue

      carton[fila][columna] = numero
      numerosCarton = numerosCarton + 1
      contador = 0

    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
          huecos = huecos + 1
      if (huecos == 3):
        return intentoCarton()

    return carton

def generar_carton():
  while True:
      carton = intentoCarton()
      if(celdas_sean_15(carton) == 15
      and fila_con_5(carton[0]) == 5
      and fila_con_5(carton[1]) == 5
      and fila_con_5(carton[2]) == 5
      and no_haya_columnas_vacias(carton)
      and no_haya_filas_vacias(carton)
      and uno_noventa(carton)
      and mayores_a_la_derecha(carton)
      and columna_may_men(carton)
      and no_haya_numero_repetido(carton)
      and no_haya_columna_llena(carton)
      and sin_3_celdas_ocupadas(carton)
      and sin_3_celdas_vacias(carton)
      and columna_sola(carton) == 3):
        break
  return carton

carton = generar_carton()