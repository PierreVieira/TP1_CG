from objetos_primeira_parte import *
from random import randint
from time import time
import globais

def deslocar():
    t = 0
    tempo = time() - globais.start
    aux = 0
    for c in range(len(all1)):
        t += all1[c]['velocidade']/randint(20,60)
        all1[c]['y'] += t - aux
        aux = t
    if int(tempo) % 2 == 0:
        todos2 = gerador_objetos(12, 12, 2.5, 1, (1, 1, 0))
        all1.append(todos2[0])