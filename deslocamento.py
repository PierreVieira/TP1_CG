from objetos_primeira_parte import *
from random import randint
import gerador_de_coordenadas1
from time import time
import globais

def deslocar():
    t = 0
    aux = 0
    for c in range(len(all1)):
        t += all1[c]['velocidade']/randint(400, 600)
        all1[c]['y'] += t - aux
        aux = t
        if all1[c]['y'] > 110:
            x_object = randint(-95, 95)
            y_object = randint(-95, -90)
            while gerador_de_coordenadas1.analise_de_proximidade(x_object, y_object, all1):
                y_object = randint(-110, -101)
                x_object = randint(-95, 95)
            all1[c]['x'] = x_object
            all1[c]['y'] = y_object