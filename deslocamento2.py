import objetos_primeira_parte
from objetos_segunda_parte import *
from random import randint, uniform
import deslocamento1
import desenheiro
from OpenGL.GL import *

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
    t = all2[c]['velocidade']*globais.cont_fora_da_tela/10000
    all2[c]['y'] -= t
    checkY2(c,x)

def deslocamento_6(c,x):
    t = all2[c]['velocidade'] * globais.cont_fora_da_tela / 10000
    all2[c]['y'] -= t
    checkY2(c,x)

def atirar(c):
    shots[c]['x'] += globais.anzol['x']/6000
    shots[c]['y'] += globais.anzol['y']/6000
    if shots[c]['y'] >= 105:
        shots[c]['visibilidade'] = True
        shots[c]['x'] = 0
        shots[c]['y'] = 0
    elif -30 <= shots[c]['y'] <= 104:
        shots[c]['x'] += shots[c]['x']/6000
        shots[c]['y'] += shots[c]['y']/6000

def move():
    for c in range(len(objetos_primeira_parte.all1)):
        deslocamento_3(c)
        for c in range(len(all2)):
            if all2[c]['id'] == 0:
                deslocamento_4(c)
            elif all2[c]['id'] == 4:
                x = randint(-160, -40)
                deslocamento_5(c,x)
            else:
                deslocamento_6(c,x+200)
        for c in range(len(lista_tiros)):
            atirar(c)