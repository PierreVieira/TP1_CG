import objetos_primeira_parte
from objetos_segunda_parte import *
from random import randint, uniform
import deslocamento1
from time import time, sleep
import texturas
from arquivos import *

def trans2():
    if all2[0]['y'] <= globais.anzol['y'] - 30:
        for c in all2:
            if c['id'] == 4:
                c['y'] += 1
    else:
        texturas.init_tex(globais.imgload[48], globais.img[48])
        sleep(1)
        globais.esta_pausado = False
        globais.estou_em_transicao = False
        globais.parte = 3

def cor_back():
    t = 0.05
    if globais.vermelho:
        globais.backg['cor'][0] -= t
        globais.backg['cor'][1] += t
        globais.backg['cor'][2] -= t
        if globais.backg['cor'][0] <= 0.2 and globais.backg['cor'][2] <= 0.2:
            globais.verde = True
            globais.vermelho = False
            globais.backg['cor'][0] = 1
            globais.backg['cor'][1] = 1
    elif globais.verde:
        globais.backg['cor'][0] -= t
        globais.backg['cor'][2] += t
        globais.backg['cor'][1] -= t
        if globais.backg['cor'][0] <= 0.2 and globais.backg['cor'][1] <= 0.2:
            globais.azul = True
            globais.verde = False
            globais.backg['cor'][0] = 1
            globais.backg['cor'][2] = 1
    elif globais.azul:
        globais.backg['cor'][1] += t
        globais.backg['cor'][0] -= t
        globais.backg['cor'][2] -= t
        if globais.backg['cor'][0] <= 0.2 and globais.backg['cor'][2] <= 0.2:
            globais.vermelho = True
            globais.azul = False
            globais.backg['cor'][1] = 1
            globais.backg['cor'][2] = 1
    else:
        globais.backg['cor'][1] -= t
        globais.backg['cor'][2] -= t
        if globais.backg['cor'][1] <= 0.2:
            globais.vermelho = True
            globais.backg['cor'][0] = 1
            globais.backg['cor'][2] = 1

def checkY2(c,x):
    if all2[c]['y'] <= -110:
        all2[c]['visivel'] = True
        all2[c]['y'] = 120
        all2[c]['x'] = x

def deslocamento_3(c): #Deslocamento caótico das lolis
    t = (uniform(0.01, 0.1) * randint(1, 10))*objetos_primeira_parte.all1[c]['velocidade']/100
    objetos_primeira_parte.all1[c]['y'] += t
    if objetos_primeira_parte.all1[c]['x'] >= 95:
        objetos_primeira_parte.all1[c]['direcao'] = False

    elif objetos_primeira_parte.all1[c]['x'] <= -95:
        objetos_primeira_parte.all1[c]['direcao'] = True

    if objetos_primeira_parte.all1[c]['direcao']:
        objetos_primeira_parte.all1[c]['x'] += t
    else:
        objetos_primeira_parte.all1[c]['x'] -= t
    deslocamento1.checkY(c)

def deslocamento_4(c): #Deslocamento Policiais
    t = all2[c]['velocidade']/randint(1, 26)
    if all2[c]['y'] >= -40: #Topo
        all2[c]['direcaoY'] = False
    elif all2[c]['y'] <= -95: #Fundo
        all2[c]['direcaoY'] = True
    if all2[c]['x'] >= 95: #Direita
        all2[c]['direcao'] = False
    elif all2[c]['x'] <= -95: #Esquerda
        all2[c]['direcao'] = True

    if all2[c]['direcaoY'] and all2[c]['direcao']:
        all2[c]['x'] += t/100
        all2[c]['y'] += t/100
    elif all2[c]['direcaoY'] and not(all2[c]['direcao']):
        all2[c]['x'] -= t/100
        all2[c]['y'] += t/100
    elif not(all2[c]['direcaoY']) and all2[c]['direcao']:
        all2[c]['x'] += t/100
        all2[c]['y'] -= t/100
    else:
        all2[c]['x'] -= t/100
        all2[c]['y'] -= t/100

def deslocamento_5(c,x): #Barricadas
    if globais.cont_fora_da_tela < 300:
        t = all2[c]['velocidade']*globais.cont_fora_da_tela/3000
    else:
        t = 0.045
    all2[c]['y'] -= t
    checkY2(c,x)

def atirar(c):
    t = shots[c]['velocidade'] / 200
    if shots[c]['y'] <= -70:
        shots[c]['y'] += t ** 2 + 0.05
        if globais.anzol['x'] >= shots[c]['x'] and globais.anzol['x'] >= 0:
            shots[c]['x'] += globais.anzol['x'] / 3000
        elif globais.anzol['x'] < shots[c]['x'] and globais.anzol['x'] >= 0:
            shots[c]['x'] -= globais.anzol['x'] / 3000
        elif globais.anzol['x'] >= shots[c]['x'] and globais.anzol['x'] < 0:
            shots[c]['x'] -= globais.anzol['x'] / 3000
        else:
            shots[c]['x'] += globais.anzol['x'] / 3000
    else:
        shots[c]['y'] += t
    if shots[c]['y'] >= 105:
        pos = randint(0, 4)
        if all2[pos]['x'] < 100:
            if all2[pos]['x'] > 0:
                shots[c]['x'] = all2[pos]['x'] - 20
            else:
                shots[c]['x'] = all2[pos]['x'] + 20
            shots[c]['y'] = all2[pos]['y'] - 8
    if analise_de_proximidade(globais.anzol['x'], globais.anzol['y'], shots, 10):
        shots[c]['visivel'] = False
        print('Distancia')
        t_col = time() - globais.start
        if t_col - globais.aux_t_col >= 1:
            print('AAIAI')
            if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                hank(globais.nomeJogador, globais.pts)
                globais.parte = 'game_over'
                return True
            qtde_vidas[0].pop(-1)
            pos = randint(0, 4)
            shots[c]['x'] = all2[pos]['x']
            shots[c]['y'] = all2[pos]['y'] + 1
            globais.aux_t_col = t_col
        shots[c]['visivel'] = True

def move():
    for c in range(len(objetos_primeira_parte.all1)):
        if randint(1, 10000) == 1:
            objetos_primeira_parte.all1[c]['id'] = 'loli_vida'
            objetos_primeira_parte.all1[c]['cor'] = (0.4, 0.4, 0.4)
        deslocamento_3(c)
        for c in range(len(all2)):
            if all2[c]['id'] == 4:
                deslocamento_4(c)
            elif all2[c]['id'] == 5:
                x = randint(-150, -50)
                deslocamento_5(c, x)
            else:
                deslocamento_5(c, x+200)
        for c in range(len(shots)):
            atirar(c)