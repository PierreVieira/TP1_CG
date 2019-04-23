from objetos_terceira_parte import *
from random import randint
import globais
from time import time
import desenheiro
import texturas

def ninja_ataca():
    t = time() - globais.start
    if t - globais.TNINJAS <= 0.3:
        globais.x = globais.anzol['x']
        globais.y = globais.anzol['y']
        desenheiro.desenha_quadrado(antes_ataque)

    elif t - globais.TNINJAS <= 1:
        antes_ataque['x'] = globais.x
        antes_ataque['y'] = globais.y
        texturas.init_tex(globais.imgload[48], globais.img[48])
        desenheiro.desenha_quadrado(antes_ataque)
    elif 1 <= t - globais.TNINJAS <= 3:
        globais.TNINJAS = t
        ataque['x'] = globais.x
        ataque['y'] = globais.y
        texturas.init_tex(globais.imgload[4], globais.img[4])
        desenheiro.desenha_quadrado(ataque)
    else:
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