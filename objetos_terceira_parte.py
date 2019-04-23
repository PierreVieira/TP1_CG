from gerador_de_objetos import gerador_objetos
from gerador_de_coordenadas1 import gerador_objetos1
import globais

qtde_ninjas = 8
todos_ninjas = []
antes_ataque = globais.quadrado.copy()
antes_ataque['id'] = 500
antes_ataque['largura'] = 15
antes_ataque['altura'] = 15
ataque = antes_ataque.copy()
ataque['id'] = 501
todos_ninjas.append(gerador_objetos(120, 1.8*14, 14, 80, qtde_ninjas, (1, 1, 0)))
ninjas = gerador_objetos1(todos_ninjas)