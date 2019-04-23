from objetos_terceira_parte import *
from random import randint
import globais
from time import time
import desenheiro

def ninja_ataca():
    if 4500 <= globais.TNINJAS <= 5500:
        ataque['x'] = globais.x
        # ataque['y'] = antes_ataque['y']
        desenheiro.desenha_quadrado(ataque)
        if globais.TNINJAS >= 1000:
            globais.TNINJAS = 0
    else:
        antes_ataque['x'] = globais.anzol['x']
        antes_ataque['y'] = globais.anzol['y']
        globais.x = antes_ataque['x']
        globais.y = antes_ataque['y']
        desenheiro.desenha_quadrado(antes_ataque)


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
            globais.TNINJAS += 1
            if randint(0,1) == 1:
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

        if (globais.n_colisoes_3+1) % 20 == 0 and globais.n_colisoes_3 <= 160:
            ninjas[0+(globais.n_colisoes_3//20)]['id'] = 120