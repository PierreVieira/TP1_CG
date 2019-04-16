from objetos_primeira_parte import *
from random import randint

def deslocar():
    tempo = 0
    aux = 0
    for c in range(len(all1)):
        tempo += all1[c]['velocidade']/randint(20,60)
        all1[c]['y'] += tempo - aux
        aux = tempo