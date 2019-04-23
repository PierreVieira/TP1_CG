import globais
from OpenGL.GLUT import *
from time import time
from menu_pause import *
from mouse import voltando_ao_inicio
import menu_pause

def tecla(key, x = 0, y = 0):
    tec = ord(key)
    if tec == 27: #ESC
        if globais.parte == 1 or globais.parte == 2 or globais.parte == 3:
            globais.esta_querendo_confirmar = True
            globais.esta_pausado = True
            globais.ultima_tecla = 27
        else:
            exit()
    elif tec == 114 or tec == 82: #r
        if globais.parte == 1 or globais.parte == 2 or globais.parte == 3:
            globais.ultima_tecla = 114
            globais.esta_querendo_confirmar = True
            globais.esta_pausado = True
        else:
            globais.parte = 'menu'
    elif (tec == 112 or tec == 80) and not(globais.estou_em_transicao): #p
        if globais.parte == 1 or globais.parte == 2 or globais.parte == 3:
            globais.esta_pausado = not(globais.esta_pausado)
            globais.esta_querendo_confirmar = False
            print('Pausando o programa')
    elif (tec == 97 or tec == 65) and not(globais.esta_pausado): #esquerda (a)
        globais.anzol['x'] -= globais.anzol['velocidade']
    elif (tec == 100 or tec == 68) and not(globais.esta_pausado): #direita (d)
        globais.anzol['x'] += globais.anzol['velocidade']
    if globais.esta_querendo_confirmar:
        if globais.ultima_tecla == 27:
            if tec == 121 or tec == 89:  # s
                exit()
            elif tec == 78 or tec == 110:  # n
                globais.esta_querendo_confirmar = False
                globais.esta_pausado = True
        elif globais.ultima_tecla == 114:
            if tec == 121 or tec == 89:  # s
                voltando_ao_inicio()
                globais.esta_pausado = False
            elif tec == 78 or tec == 110:  # n
                globais.esta_querendo_confirmar = False
                globais.esta_pausado = True

def movimenta_anzol(self, key, x = 0, y = 0):
    if not(globais.esta_pausado):
        if self == GLUT_KEY_UP and globais.anzol['y'] <= 90:
            globais.anzol['y'] += globais.anzol['velocidade']
        elif self == GLUT_KEY_DOWN and globais.anzol['y'] >= -90:
            globais.anzol['y'] -= globais.anzol['velocidade']
        elif self == GLUT_KEY_LEFT and globais.anzol['x'] >= -90: #seta esquerda
            globais.anzol['x'] -= globais.anzol['velocidade']
        elif self == GLUT_KEY_RIGHT and globais.anzol['x'] <= 90: #seta direita
            globais.anzol['x'] += globais.anzol['velocidade']

def movimenta_vergil(self, key, x = 0, y = 0):
    if not(globais.esta_pausado):
        if self == GLUT_KEY_UP and globais.vergil['y'] <= 90:
            globais.vergil['y'] += globais.vergil['velocidade']
        elif self == GLUT_KEY_DOWN and globais.vergil['y'] >= -90:
            globais.vergil['y'] -= globais.vergil['velocidade']
        elif self == GLUT_KEY_LEFT and globais.vergil['x'] >= -90: #seta esquerda
            globais.vergil['x'] -= globais.vergil['velocidade']
        elif self == GLUT_KEY_RIGHT and globais.vergil['x'] <= 90: #seta direita
            globais.vergil['x'] += globais.vergil['velocidade']