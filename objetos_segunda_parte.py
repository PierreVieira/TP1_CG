from gerador_de_objetos import gerador_objetos
from gerador_de_coordenadas2 import gerador_objetos2
import globais
from random import randint

qtde_policiais = 5
todos2 = []
barricada_e = globais.quadrado.copy()
barricada_e['altura'] = 12
barricada_e['cor'] = (0, 1, 0)
barricada_e['id'] = 4
barricada_e['largura'] = 150
barricada_e['y'] = 120
barricada_d = barricada_e.copy()
todos2.append((gerador_objetos(11, 11, 5, qtde_policiais, (0, 0, 0))))
todos2[0].append(barricada_e)
todos2[0].append(barricada_d)
all2 = gerador_objetos2(todos2)