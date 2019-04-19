import objetos_primeira_parte
from objetos_segunda_parte import *
from random import randint, uniform
import deslocamento1

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
    print(t)
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
    elif all2[c]['direcaoY'] and not(all2[c]['direcao']) :
        all2[c]['x'] -= t/100
        all2[c]['y'] += t/100
    elif not(all2[c]['direcaoY']) and all2[c]['direcao']:
        all2[c]['x'] += t/100
        all2[c]['y'] -= t/100
    else:
        all2[c]['x'] -= t/100
        all2[c]['y'] -= t/100

def move():
    for c in range(len(objetos_primeira_parte.all1)):
        deslocamento_3(c)
        for c in range(len(all2)):
            if all2[c]['id'] == 0:
                deslocamento_4(c)
            elif all2[c]['id'] == 5:
                deslocamento_5(c)
