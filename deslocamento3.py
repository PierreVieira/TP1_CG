from objetos_terceira_parte import *
from random import randint
import globais
from time import time


def verificar_tempo(quadrado):
    tempo = globais.start - time()
    if int(tempo)%2 == 0:
        quadrado['visivel'] = True


def mov_ninjas():
    for c in range(len(ninjas)):
        t = (ninjas[c]['velocidade']/randint(1, 10))
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