from objetos_terceira_parte import *
from random import randint
import globais
from time import time


def verificar_tempo(quadrado):
    tempo = globais.start - time()
    if int(tempo)%2 == 0:
        quadrado['visivel'] = True


def mov_ninjas_lolis(c):
    r = 12
    t = ninjas[c]['velocidade']/randint(50, 200)
    ninjas[c]['x'] = (r**2 - (ninjas[c]['y']/10)**2)**0.5
    if globais.anzol['y'] >= ninjas[c]['y']:
        ninjas[c]['y'] -= t/100
    else:
        ninjas[c]['y'] += t/100


def mov_ninjas():
    for c in range(len(ninjas)):
        if ninjas[c]['id'] == 120:
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

        if (globais.n_colisoes_3+1) % 20 == 0 and globais.n_colisoes_3 <= 160:
            ninjas[0+(globais.n_colisoes_3//20)]['id'] = 120