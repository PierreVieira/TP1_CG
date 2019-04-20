import globais
from OpenGL.GLUT import *
from time import time
from colisao import *
from menu_pause import *
from globais import *
import menu_pause
def conversao(x, y):
    if x < 300:
        x = -(100 -x/3)
    else:
        x = x/3 - 100
    if y < 300:
        y = 100 - y/3
    else:
        y = -(y/3 - 100)
    return (x, y)

def movimentoMouse(x, y):
    x, y = conversao(x, y)
    seguidor_mouse['x'] = x
    seguidor_mouse['y'] = y

def clicks_do_mouse(button, state, x, y):
    x, y = conversao(x, y)
    print(x, y)
    if collision(seguidor_mouse, botao_iniciar_jogo):
        globais.parte = 1
    elif collision(seguidor_mouse, botao_creditos):
        globais.parte = -1
    elif collision(seguidor_mouse, botao_sair):
        exit()
    else:
        globais.parte = 0