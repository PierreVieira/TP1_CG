from gerador_de_objetos import gerador_objetos
from gerador_de_coordenadas2 import *
import globais
from random import randint

qtde_policiais = 5
todos2 = []
lista_tiros = []
lista_pts = []
qtde_vidas = []
vida = globais.quadrado.copy()
vida['y'] = 95
vida['id'] = 8
vida['altura'] = 5
vida['largura'] = 5
vida['cor'] = (0, 0, 0)
lpts = globais.quadrado.copy()
lpts['y'] = 95
lpts['id'] = 10
lpts['altura'] = 5
lpts['largura'] = 5
lpts['cor'] = (0, 0, 0)
lpts1 = lpts.copy()
lpts1['id'] = 11
lpts2 = lpts.copy()
lpts2['id'] = 12
lpts3 = lpts.copy()
lpts3['id'] = 13

tiro = globais.quadrado.copy()
barricada_e = globais.quadrado.copy()
barricada_e['altura'] = 8
barricada_e['cor'] = (0, 1, 0)
barricada_e['id'] = 5
barricada_e['largura'] = 100
barricada_e['velocidade'] = 0.5
barricada_e['y'] = 120
barricada_e['x'] = -100
d = 200 - barricada_e['largura']
barricada_d = barricada_e.copy()
barricada_d['x'] = 100
barricada_d['id'] = 6

todos2.append((gerador_objetos(4, 15, 15, 15, qtde_policiais, (0, 0, 0))))
todos2[0].append(barricada_e)
todos2[0].append(barricada_d)
all2 = gerador_objetos2(todos2)

lista_tiros.append((gerador_objetos(7, 6, 2, 4, qtde_policiais, (0, 0, 0))))
shots = coord_tiro(lista_tiros)

qtde_vidas.append((gerador_objetos(8, 5, 5, 0, 25, (1, 1, 1))))
lives = coord_lives(qtde_vidas)

lista_pts.append((gerador_objetos(10, 5, 5, 0, 1, (1, 1, 1))))
lista_pts[0].extend((lpts1, lpts2, lpts3))
PTS = coord_pts(lista_pts)