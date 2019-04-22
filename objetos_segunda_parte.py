from gerador_de_objetos import gerador_objetos
from gerador_de_coordenadas2 import *
import globais
from random import randint

qtde_policiais = 5
todos2 = []
lista_tiros = []
qtde_vidas = []
vida = globais.quadrado.copy()
vida['y'] = 95
vida['id'] = 8
vida['altura'] = 5
vida['largura'] = 5
vida['cor'] = (0, 0, 0)
tiro = globais.quadrado.copy()
barricada_e = globais.quadrado.copy()
barricada_e['altura'] = 8
barricada_e['cor'] = (0, 1, 0)
barricada_e['id'] = 5
barricada_e['largura'] = 100
barricada_e['velocidade'] = 1
barricada_e['y'] = 120
barricada_e['x'] = -100
d = 200 - barricada_e['largura']
barricada_d = barricada_e.copy()
barricada_d['x'] = 100
barricada_d['id'] = 6

todos2.append((gerador_objetos(4, 11, 11, 9, qtde_policiais, (0, 0, 0))))
todos2[0].append(barricada_e)
todos2[0].append(barricada_d)
all2 = gerador_objetos2(todos2)

lista_tiros.append((gerador_objetos(7, 6, 2, 5, qtde_policiais, (0, 0, 0))))
shots = coord_tiro(lista_tiros)

qtde_vidas.append((gerador_objetos(8, 5, 5, 0, 35, (1, 1, 1))))
lives = coord_lives(qtde_vidas)