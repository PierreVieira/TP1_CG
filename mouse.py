from colisao import *
from menu_pause import *
from globais import *
from pygame import mixer
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
    if button == GLUT_LEFT_BUTTON:
        if globais.parte == 'menu':
            if collision(seguidor_mouse, botao_iniciar_jogo):
                globais.parte = 1
                globais.aux_musica = True
            elif collision(seguidor_mouse, botao_creditos):
                globais.parte = 'creditos'
                globais.aux_musica = True
            elif collision(seguidor_mouse, botao_sair):
                exit()
            elif collision(seguidor_mouse, botao_instrucoes):
                globais.parte = 'instrucoes'
            elif collision(seguidor_mouse, botao_ranking):
                globais.parte = 'ranking'
    elif button == GLUT_RIGHT_BUTTON and not(globais.parte == 1 or globais.parte == 2 or globais.parte == 3):
        globais.aux_musica = True
        globais.parte = 'menu'