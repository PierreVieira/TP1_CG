from objetos_terceira_parte import *
from random import randint
import globais
from time import time
import desenheiro
import texturas
import gerador_de_coordenadas1
import colisao

def ninja_ataca():
    t = time() - globais.start
    texturas.init_tex(globais.imgload[48], globais.img[48])
    if t - globais.TNINJAS <= 0.3:
        globais.x = globais.anzol['x']
        globais.y = globais.anzol['y']
        desenheiro.desenha_quadrado(antes_ataque)

    elif t - globais.TNINJAS <= 1:
        antes_ataque['x'] = globais.x
        antes_ataque['y'] = globais.y
        desenheiro.desenha_quadrado(antes_ataque)
    elif 1 <= t - globais.TNINJAS <= 3:
        globais.TNINJAS = t
        ataque['x'] = globais.x
        ataque['y'] = globais.y
        texturas.init_tex(globais.imgload[4], globais.img[4])
        desenheiro.desenha_quadrado(ataque)
        if colisao.collision(globais.anzol, ataque):
            globais.qtde_vidas[0].pop(-1)
    else:
        globais.TNINJAS = t
        globais.AUX = 0


def verificar_tempo(quadrado):
    tempo = globais.start - time()
    if int(tempo)%2 == 0:
        quadrado['visivel'] = True


def mov_ninjas_lolis(c):
    t = ninjas[c]['velocidade'] / 500
    if ninjas[c]['x'] >= globais.anzol['x'] + 40 and ninjas[c]['y'] >= globais.anzol['y'] + 40:
        ninjas[c]['x'] -= t + globais.anzol['y'] / 1000
        ninjas[c]['y'] -= t + globais.anzol['x'] / 1000
    elif ninjas[c]['x'] <= globais.anzol['x'] - 40 and ninjas[c]['y'] >= globais.anzol['y'] + 40:
        ninjas[c]['x'] += t + globais.anzol['y'] / 1000
        ninjas[c]['y'] -= t + globais.anzol['x'] / 1000
    elif ninjas[c]['x'] >= globais.anzol['x'] + 40 and ninjas[c]['y'] <= globais.anzol['y'] - 40:
        ninjas[c]['x'] -= t + globais.anzol['y'] / 1000
        ninjas[c]['y'] += t + globais.anzol['x'] / 1000
    elif ninjas[c]['x'] <= globais.anzol['x'] + 40 and ninjas[c]['y'] <= globais.anzol['y'] - 40:
        ninjas[c]['x'] += t + globais.anzol['y'] / 1000
        ninjas[c]['y'] += t + globais.anzol['x'] / 1000


def mov_ninjas():
    for c in range(len(ninjas)):
        if ninjas[c]['id'] == 120:
            if randint(0, 100) == 1 or globais.AUX:
                globais.AUX = 1
                ninja_ataca()
            mov_ninjas_lolis(c)
        elif ninjas[c]['id'] == 130:
            t = ninjas[c]['velocidade'] / randint(400, 1200)
            ninjas[c]['y'] += t * 5
            if int(time() - globais.start) % 2 == 0:
                ninjas[c]['direcao'] = True
            else:
                ninjas[c]['direcao'] = False

            if ninjas[c]['direcao']:
                ninjas[c]['x'] += (t ** 2) * 5
            else:
                ninjas[c]['x'] -= (t ** 2) * 5

            if ninjas[c]['y'] >= 110:
                globais.cont_fora_da_tela += 1
                ninjas[c]['visivel'] = True
                x_object = randint(-95, 95)
                y_object = randint(-95, -90)
                while gerador_de_coordenadas1.analise_de_proximidade(x_object, y_object, ninjas, 30):
                    y_object = randint(-110, -101)
                    x_object = randint(-95, 95)
                ninjas[c]['x'] = x_object
                ninjas[c]['y'] = y_object
                if globais.parte == 2:
                    ninjas[c]['id'] = randint(0, 3)
                    ninjas[c]['cor'] = (1, 1, 0)

        else:
            t = (ninjas[c]['velocidade']/5)
            if ninjas[c]['y'] >= 95: #Topo
                ninjas[c]['direcaoY'] = False
            elif ninjas[c]['y'] <= -95: #Fundo
                ninjas[c]['direcaoY'] = True
            if ninjas[c]['x'] >= 95: #Direita
                ninjas[c]['direcao'] = False
            elif ninjas[c]['x'] <= -95: #Esquerda
                ninjas[c]['direcao'] = True

            if ninjas[c]['direcaoY'] and ninjas[c]['direcao']:
                ninjas[c]['x'] += t/100
                ninjas[c]['y'] += t/100
            elif ninjas[c]['direcaoY'] and not(ninjas[c]['direcao']):
                ninjas[c]['x'] -= t/100
                ninjas[c]['y'] += t/100
            elif not(ninjas[c]['direcaoY']) and ninjas[c]['direcao']:
                ninjas[c]['x'] += t/100
                ninjas[c]['y'] -= t/100
            else:
                ninjas[c]['x'] -= t/100
                ninjas[c]['y'] -= t/100

        if (globais.n_colisoes_3+1) % 20 == 0 and globais.n_colisoes_3 <= 40:
            ninjas[0+(globais.n_colisoes_3//20)]['id'] = 120
            ninjas[0+(globais.n_colisoes_3//20)]['n_colisoes'] = -70
        elif (globais.n_colisoes_3+1) % 20 == 0 and 40 <= globais.n_colisoes_3 <= 80:
            ninjas[2 + (globais.n_colisoes_3 // 20)]['id'] = 130
            ninjas[2 + (globais.n_colisoes_3 // 20)]['n_colisoes'] = -70