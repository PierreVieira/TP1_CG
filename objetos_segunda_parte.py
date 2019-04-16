from gerador_de_objetos import gerador_objetos
from gerador_de_coordenadas2 import gerador_objetos2
qtde_peixes = 8
lista_peixes = []
lista_peixes.append(gerador_objetos(12, 12, 5, qtde_peixes, (1, 1, 0)))
lista_traps = []
lista_traps.append(gerador_objetos(12, 12, 5, qtde_peixes//2, (0, 0, 0)))
todos = gerador_objetos2(lista_peixes, lista_traps)
