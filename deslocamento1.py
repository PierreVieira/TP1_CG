from objetos_primeira_parte import *
from random import randint
import gerador_de_coordenadas1
import globais
from time import time, sleep

def deslocar_camburao(camburao):
    if camburao['y'] < -80:
        camburao['y'] += camburao['velocidade']/2
    else:
        all1.pop(-1)
        sleep(1)
        globais.parte = 2
        globais.estou_em_transicao = False
        globais.esta_pausado = False
    globais.esta_querendo_confirmar = False
    print(globais.pts)

def checkY(c):
    if all1[c]['y'] >= 110:
        globais.cont_fora_da_tela += 1
        all1[c]['visivel'] = True
        x_object = randint(-95, 95)
        y_object = randint(-95, -90)
        while gerador_de_coordenadas1.analise_de_proximidade(x_object, y_object, all1, 26):
            y_object = randint(-110, -101)
            x_object = randint(-95, 95)
        all1[c]['x'] = x_object
        all1[c]['y'] = y_object
        if globais.parte == 2:
            all1[c]['id'] = 0
            all1[c]['cor'] = (1, 1, 0)

def deslocamento_0(c):
    t = 0
    t += all1[c]['velocidade'] / randint(200, 600)
    all1[c]['y'] += t
    checkY(c)

def deslocamento_1(c):
    t = all1[c]['velocidade'] / randint(400, 1200)
    all1[c]['y'] += t*2

    if all1[c]['x'] >= 95:
        all1[c]['direcao'] = False

    elif all1[c]['x'] <= -95:
        all1[c]['direcao'] = True

    if all1[c]['direcao']:
        all1[c]['x'] += t
    else:
        all1[c]['x'] -= t
    checkY(c)

def deslocamento_2(c):
    t = all1[c]['velocidade'] / randint(400, 1200)
    all1[c]['y'] += t*5
    if int(time() - globais.start) % 2 == 0:
        all1[c]['direcao'] = True
    else:
        all1[c]['direcao'] = False

    if all1[c]['direcao']:
        all1[c]['x'] += (t**2)*5
    else:
        all1[c]['x'] -= (t**2)*5
    checkY(c)

def deslocar(apenas_caminhao):
    globais.pts = globais.multiplicador_pts1*globais.cont_fora_da_tela
    for c in range(len(all1)):
        if all1[c]['id'] == 0 and not(apenas_caminhao):
            deslocamento_0(c)
        elif all1[c]['id'] == 1 and not(apenas_caminhao):
            deslocamento_1(c)
        elif all1[c]['id'] == 2 and not(apenas_caminhao):
            deslocamento_2(c)
        elif all1[c]['id'] == 3:
            deslocar_camburao(all1[c])
        if (globais.cont_fora_da_tela+1) % 20 == 0 and globais.cont_fora_da_tela <= 80:
            globais.multiplicador_pts1 += 0.001
            all1[0+(globais.cont_fora_da_tela//20)]['id'] = 1
            all1[0+(globais.cont_fora_da_tela//20)]['cor'] = (1, 0, 1)

        elif (globais.cont_fora_da_tela+1) % 20 == 0 and 80 <= globais.cont_fora_da_tela <= 160:
            globais.multiplicador_pts1 += 0.0035
            all1[4 + (globais.cont_fora_da_tela // 20)]['id'] = 2
            all1[4 + (globais.cont_fora_da_tela // 20)]['cor'] = (0, 0, 0)