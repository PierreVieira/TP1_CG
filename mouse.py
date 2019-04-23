from colisao import *
from menu_pause import *
import menu_confi
from globais import *
import objetos_primeira_parte
from pygame import mixer
def conversao(x, y):
    if x < 300:
        x = -(100 -x/3)
    else:
        x = x/3 - 100
    if y < 350:
        y = 100 - y/3.5
    else:
        y = -(y/3.5 - 100)
    return (x, y)
def reorganizar(lista):
    for c in range(len(lista)):
        x_object = randint(-95, 95)
        y_object = randint(-95, 0)
        while(analise_de_proximidade(x_object, y_object, lista, 22)):
            x_object = randint(-95, 95)
            y_object = randint(-95, 0)
        lista[c]['x'] = x_object
        lista[c]['y'] = y_object
    return lista

def voltando_ao_inicio():
    globais.parte = 'menu'
    globais.cont_fora_da_tela = 0
    nova_lista = []
    for c in objetos_primeira_parte.all1:
        nova_lista.append(c)
    objetos_primeira_parte.all1 = reorganizar(nova_lista)
    globais.esta_pausado = not (globais.esta_pausado)
    globais.aux_musica = True

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
        if globais.esta_pausado:
            if collision(seguidor_mouse, voltar_menu_principal):
                globais.esta_querendo_confirmar = False
                globais.ultima_tecla = 114
                voltando_ao_inicio()
            elif collision(seguidor_mouse, audio_switchE):
                mixer.music.set_volume(0)
            elif collision(seguidor_mouse, audio_switchD):
                mixer.music.set_volume(100)
            elif collision(seguidor_mouse, quitar_game):
                globais.esta_querendo_confirmar = True
                globais.ultima_tecla = 27
    elif button == GLUT_RIGHT_BUTTON and not(globais.parte == 1 or globais.parte == 2 or globais.parte == 3):
        globais.aux_musica = True
        globais.parte = 'menu'