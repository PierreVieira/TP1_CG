from objetos_primeira_parte import *
from random import randint
import gerador_de_coordenadas1
import globais

def deslocamento_0(c):
    t = aux = 0
    t += all1[c]['velocidade'] / randint(200, 600)
    all1[c]['y'] += t - aux
    aux = t
    if all1[c]['y'] > 110:
        globais.cont_fora_da_tela +=1
        all1[c]['visivel'] = True
        x_object = randint(-95, 95)
        y_object = randint(-95, -90)
        while gerador_de_coordenadas1.analise_de_proximidade(x_object, y_object, all1):
            y_object = randint(-110, -101)
            x_object = randint(-95, 95)
        all1[c]['x'] = x_object
        all1[c]['y'] = y_object

def deslocamento_1(c):
    t = aux = 0
    hit = False
    t += all1[c]['velocidade'] / randint(200, 600)
    all1[c]['y'] += t - aux

    if abs(all1[c]['x']) == 95:
        hit = not(hit)

    if hit:
        all1[c]['x'] -= t
    else:
        all1[c]['x'] += t

    if all1[c]['y'] > 110:
        globais.cont_fora_da_tela += 1
        all1[c]['visivel'] = True
        x_object = randint(-95, 95)
        y_object = randint(-95, -90)
        while gerador_de_coordenadas1.analise_de_proximidade(x_object, y_object, all1):
            y_object = randint(-110, -101)
            x_object = randint(-95, 95)
        all1[c]['x'] = x_object
        all1[c]['y'] = y_object


def deslocar():
    for c in range(len(all1)):
        if all1[c]['id'] == 0:
            deslocamento_0(c)
        if globais.cont_fora_da_tela == 4:
            all1[0]['id'] = 1
            all1[0]['cor'] = (1, 0, 1)
        elif all1[c]['id'] == 1:
            deslocamento_1(c)

