from gerador_de_objetos import gerador_objetos
from gerador_de_coordenadas2 import *
import globais
from random import randint

qtde_policiais = 5
todos2 = []
lista_tiros = []
tiro = globais.quadrado.copy()
barricada_e = globais.quadrado.copy()
barricada_e['altura'] = 8
barricada_e['cor'] = (0, 1, 0)
barricada_e['id'] = 4
barricada_e['largura'] = 80
barricada_e['velocidade'] = 1
barricada_e['y'] = 120
barricada_e['x'] = -100
d = 200 - barricada_e['largura']
barricada_d = barricada_e.copy()
barricada_d['x'] = 100
barricada_d['id'] = 5

todos2.append((gerador_objetos(11, 11, 5, qtde_policiais, (0, 0, 0))))
todos2[0].append(barricada_e)
todos2[0].append(barricada_d)
all2 = gerador_objetos2(todos2)

lista_tiros.append((gerador_objetos(6, 2, 5, 2, (0, 0, 0))))
shots = coord_tiro(lista_tiros)
