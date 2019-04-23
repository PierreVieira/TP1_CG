from objetos_terceira_parte import *
import objetos_segunda_parte
from random import randint
import globais
from time import time
import desenheiro
import texturas
import gerador_de_coordenadas1
import colisao
from arquivos import *
from math import *
def ninja_ataca():
    if globais.VT <= 1000:
        globais.VT += 1
    else:
        globais.VT = 0
    texturas.init_tex(globais.imgload[48], globais.img[48])
    if globais.VT <= 30:
        globais.x = globais.anzol['x']
        globais.y = globais.anzol['y']

    elif globais.VT <= 160:
        antes_ataque['x'] = globais.x
        antes_ataque['y'] = globais.y
        desenheiro.desenha_quadrado(antes_ataque)
    elif globais.VT <= 200:
        globais.HP += 0.1
        ataque['x'] = globais.x
        ataque['y'] = globais.y
        texturas.init_tex(globais.imgload[4], globais.img[4])
        desenheiro.desenha_quadrado(ataque)
        if colisao.collision(globais.anzol, ataque):
            if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                hank(globais.nomeJogador, globais.pts)
                exit()
            objetos_segunda_parte.qtde_vidas[0].pop(-1)
    else:
        globais.AUX = 0


def verificar_tempo(quadrado):
    quadrado['tempo_morte'] = time() - globais.start
    if int(quadrado['tempo_morte'])%quadrado['tempo_resp'] == 0:
        quadrado['visivel'] = True
        quadrado['tempo_morte'] = 0

def mov_ninjas_lolis(c):
    t = ninjas[c]['velocidade'] / 5000
    r = 40
    globais.s += t
    ninjas[c]['x'] = globais.anzol['x'] + r*cos(globais.s)
    ninjas[c]['y'] = globais.anzol['y'] + r*sin(globais.s)


def mov_ninjas():
    for c in range(len(ninjas)):
        if colisao.collision(globais.anzol, ninjas[c]):
            globais.HP += 0.1
            if globais.HP >= 1:
                globais.HP = 0
                if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                    hank(globais.nomeJogador, globais.pts)
                    exit()
                objetos_segunda_parte.qtde_vidas[0].pop(-1)
        if ninjas[c]['id'] == 120:
            if randint(0, 1000) == 1 or globais.AUX:
                globais.AUX = 1
                ninja_ataca()
            mov_ninjas_lolis(c)
        elif ninjas[c]['id'] == 130:
            if colisao.collision(globais.anzol, ninjas[c]):
                globais.HP += 0.3
                if globais.HP >= 1:
                    globais.HP = 0
                    if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                        hank(globais.nomeJogador, globais.pts)
                        exit()
                    objetos_segunda_parte.qtde_vidas[0].pop(-1)
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
                ninjas[c]['x'] += t/60
                ninjas[c]['y'] += t/60
            elif ninjas[c]['direcaoY'] and not(ninjas[c]['direcao']):
                ninjas[c]['x'] -= t/60
                ninjas[c]['y'] += t/60
            elif not(ninjas[c]['direcaoY']) and ninjas[c]['direcao']:
                ninjas[c]['x'] += t/60
                ninjas[c]['y'] -= t/60
            else:
                ninjas[c]['x'] -= t/60
                ninjas[c]['y'] -= t/60

        if (globais.n_colisoes_3+1) % 20 == 0 and globais.n_colisoes_3 <= 20:
            ninjas[0+(globais.n_colisoes_3//20)]['id'] = 120
            ninjas[0+(globais.n_colisoes_3//20)]['n_colisoes'] = -70
            ninjas[0 + (globais.n_colisoes_3 // 20)]['tempo_resp'] = 10
        elif (globais.n_colisoes_3+1) % 20 == 0 and 20 <= globais.n_colisoes_3 <= 60:
            ninjas[2 + (globais.n_colisoes_3 // 20)]['id'] = 130
            ninjas[2 + (globais.n_colisoes_3 // 20)]['n_colisoes'] = -70
            ninjas[2 + (globais.n_colisoes_3 // 20)]['tempo_resp'] = 6