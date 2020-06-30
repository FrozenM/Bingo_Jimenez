from jinja2 import Template
from src.bingo import *

template = Template(open('src/mostrar.j2').read())

carton2 = template.render(tablero=generar_carton())

file = open("Bingo_terminado.html","w")

file.write(carton2)

file.close()