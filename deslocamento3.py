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
    if globais.VT <= 300:
        globais.VT += 1
    else:
        globais.VT = 0
        globais.AUX = 0
    texturas.init_tex(globais.imgload[48], globais.img[48])
    if globais.VT <= 30:
        globais.x = globais.anzol['x']
        globais.y = globais.anzol['y']

    elif globais.VT <= 80:
        antes_ataque['x'] = globais.x
        antes_ataque['y'] = globais.y
        desenheiro.desenha_quadrado(antes_ataque)
    elif globais.VT <= 150:
        antes_ataque['x'] = globais.x
        antes_ataque['y'] = globais.y
        desenheiro.desenha_quadrado(antes_ataque, 1)
    elif 230 <= globais.VT <= 300:
        ataque['x'] = globais.x
        ataque['y'] = globais.y
        texturas.init_tex(globais.imgload[73], globais.img[73])
        desenheiro.desenha_quadrado(ataque)
        if globais.VT <= 260:
            texturas.init_tex(globais.imgload[73], globais.img[73])
        elif globais.VT <= 280:
            texturas.init_tex(globais.imgload[74], globais.img[74])
        else:
            texturas.init_tex(globais.imgload[75], globais.img[75])


def verificar_tempo(quadrado):
    quadrado['tempo_morte'] = time() - globais.start
    if int(quadrado['tempo_morte']) % quadrado['tempo_resp'] == 0:
        quadrado['visivel'] = True
        quadrado['tempo_morte'] = 0

def mov_ninjas_lolis(c):
    t = ninjas[c]['velocidade'] / 5000
    r = 40
    globais.s += t
    ninjas[c]['x'] = globais.anzol['x'] + r*cos(globais.s)
    ninjas[c]['y'] = globais.anzol['y'] + r*sin(globais.s)


def mov_ninjas():
    if globais.backg2['y'] >= 100:
        globais.aux_back = True
    elif globais.backg2['y'] <= -100:
        globais.aux_back = False
    if globais.aux_back:
        globais.backg2['y'] -= 0.1
    else:
        globais.backg2['y'] += 0.1

    for c in range(len(ninjas)):
        if colisao.collision(globais.anzol, ninjas[c]):
            globais.HP += 0.01
            if globais.HP >= 1:
                globais.HP = 0
                if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                    hank(globais.nomeJogador, globais.pts)
                    globais.parte = 'game_over'
                    return True
                objetos_segunda_parte.qtde_vidas[0].pop(-1)
        if ninjas[c]['id'] == 100:
            ninjas[c]['temp_resp'] = 5
        if ninjas[c]['id'] == 120 and ninjas[c]['visivel']:
            if randint(0, 150) == 1 or globais.AUX:
                globais.AUX = 1
                ninja_ataca()
            mov_ninjas_lolis(c)
        elif ninjas[c]['id'] == 130:
            if colisao.collision(globais.anzol, ninjas[c]):
                globais.HP += 0.006
                if globais.HP >= 1:
                    globais.HP = 0
                    if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                        hank(globais.nomeJogador, globais.pts)
                        globais.parte = 'game_over'
                        return True
                    objetos_segunda_parte.qtde_vidas[0].pop(-1)
            t = ninjas[c]['velocidade'] / 350
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
            t = (ninjas[c]['velocidade']/3.5)
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

        if (globais.n_colisoes_3+1) % 60 == 0 and globais.n_colisoes_3 <= 60:
            ninjas[0+(globais.n_colisoes_3//60)]['id'] = 120
            ninjas[0+(globais.n_colisoes_3//60)]['n_colisoes'] = -70
            ninjas[0 + (globais.n_colisoes_3 // 60)]['tempo_resp'] = 20
        elif (globais.n_colisoes_3+1) % 60 == 0 and 60 < globais.n_colisoes_3 <= 180:
            ninjas[2 + (globais.n_colisoes_3 // 60)]['id'] = 130
            ninjas[2 + (globais.n_colisoes_3 // 60)]['n_colisoes'] = -70
            ninjas[2 + (globais.n_colisoes_3 // 60)]['tempo_resp'] = 6