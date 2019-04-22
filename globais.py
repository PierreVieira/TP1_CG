from OpenGL.GLUT import *
from OpenGL.GL import *
import time
import pygame

def text_e(imgload):
    img = pygame.image.tostring(imgload, 'RGBA', 1)
    return img

aux_musica = True
imgload = []
img = []
imgload.append(pygame.image.load('Os trem/Loli1_parte1.png'))
img.append(text_e(imgload[0]))
imgload.append(pygame.image.load('Os trem/Loli2_parte1.png'))
img.append(text_e(imgload[1]))
imgload.append(pygame.image.load('Os trem/Tokyo-compressed.jpg'))
img.append(text_e(imgload[2]))
imgload.append(pygame.image.load('Os trem/menu_loli.jpg'))
img.append(text_e(imgload[3]))
imgload.append(pygame.image.load('Os trem/play_button.png'))
img.append(text_e(imgload[4]))
imgload.append(pygame.image.load('Os trem/Ranking_button.png'))
img.append(text_e(imgload[5]))
imgload.append(pygame.image.load('Os trem/Kita_png.png'))
img.append(text_e(imgload[6]))
imgload.append(pygame.image.load('Os trem/Instruções.png'))
img.append(text_e(imgload[7]))
imgload.append(pygame.image.load('Os trem/Créditos_button.png'))
img.append(text_e(imgload[8]))
imgload.append(pygame.image.load('Os trem/pause_fundo.png'))
img.append(text_e(imgload[9]))
imgload.append(pygame.image.load('Os trem/menu_principal.png'))
img.append(text_e(imgload[10]))
imgload.append(pygame.image.load('Os trem/sound_feito.png'))
img.append(text_e(imgload[11]))
imgload.append(pygame.image.load('Os trem/mute_feito.png'))
img.append(text_e(imgload[12]))
imgload.append(pygame.image.load('Os trem/quitar.png'))
img.append(text_e(imgload[13]))
imgload.append(pygame.image.load('Os trem/LoliEncostou.png'))
img.append(text_e(imgload[14]))
imgload.append(pygame.image.load('Os trem/desesperada.png'))
img.append(text_e(imgload[15]))
imgload.append(pygame.image.load('Os trem/Yare.jpg'))
img.append(text_e(imgload[16]))
imgload.append(pygame.image.load('Os trem/Danashi1-1.png'))
img.append(text_e(imgload[17]))

imgload.append(pygame.image.load('Os trem/zero.png'))
img.append(text_e(imgload[18]))
imgload.append(pygame.image.load('Os trem/um.png'))
img.append(text_e(imgload[19]))
imgload.append(pygame.image.load('Os trem/dois.png'))
img.append(text_e(imgload[20]))
imgload.append(pygame.image.load('Os trem/tres.png'))
img.append(text_e(imgload[21]))
imgload.append(pygame.image.load('Os trem/quatro.png'))
img.append(text_e(imgload[22]))
imgload.append(pygame.image.load('Os trem/cinco.png'))
img.append(text_e(imgload[23]))
imgload.append(pygame.image.load('Os trem/seis.png'))
img.append(text_e(imgload[24]))
imgload.append(pygame.image.load('Os trem/sete.png'))
img.append(text_e(imgload[25]))
imgload.append(pygame.image.load('Os trem/oito.png'))
img.append(text_e(imgload[26]))
imgload.append(pygame.image.load('Os trem/nove.png'))
img.append(text_e(imgload[27]))

glutInit()
pts = 324
multiplicador_pts1 = 1
multiplicador_pts2 = 1
qtde_lolis_capturadas = 0
aux_tempo_alternacao1 = 0
aux_t_col = 0
alterna_loli = True
ultima_tecla = 0
start = time.time()
esta_pausado = False
esta_querendo_confirmar = False
estou_em_transicao = False
parte = 'menu'
cont_fora_da_tela = 0
quadrado = {
    'id_text': 0,
    'id': 0, #int
    'x': 0, #float
    'y': 0, #float
    'largura': 0, #float
    'altura': 0, #float
    'visivel':True, #booleano
    'velocidade': 0, #float/int
    'area': 0, #float
    'n_colisoes': 0,
    'direcao': True,
    'direcaoY': True,
    'cor': (0, 0, 0)
}
#Definição de um botão interativo
interavel = quadrado.copy()
interavel['x'] = 150 #desenhar o mouse inicialmente fora da tela
interavel['cor'] = (1, 0, 0)


#Definindo um objeto para seguir o mouse
seguidor_mouse = quadrado.copy()
seguidor_mouse['cor'] = (0, 0, 1)
seguidor_mouse['largura'] = 4
seguidor_mouse['altura'] = 4


#Definindo um quadrado para as telas
tela_inicial = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (0, 0, 0)}
tela_creditos = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (0, 0, 1)}
tela_instrucoes = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (1, 0, 1)}
tela_ranking = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (0, 1, 0)}

#Definição de fundos
backg = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (1, 0, 1), 'id': 8}

#Definindo o meu anzol
anzol = quadrado.copy()
anzol['x'] = 20
anzol['y'] = 90
anzol['altura'] = 8
anzol['visivel'] = True
anzol['largura'] = 8
anzol['velocidade'] = 8
anzol['cor'] = (1, 1, 1)
anzol['id'] = 'anzol'

#Definição de botões

#Definição do botão que inicializa o jogo
botao_iniciar_jogo = quadrado.copy()
botao_iniciar_jogo['id'] = 'btnInicializador'
botao_iniciar_jogo['x'] = 0
botao_iniciar_jogo['y'] = 0
botao_iniciar_jogo['largura'] = 60
botao_iniciar_jogo['altura'] = 25
botao_iniciar_jogo['cor'] = (0, 1, 1)

#Definição de um botão que vai para a tela de créditos
botao_creditos = botao_iniciar_jogo.copy()
botao_creditos['id'] = 'btnCreditos'
botao_creditos['x'] = -70
botao_creditos['y'] = 0

#Definição de um botão que vai acessa o ranking
botao_ranking = botao_iniciar_jogo.copy()
botao_ranking['id'] = 'btnRanking'
botao_ranking['x'] = 70
botao_ranking['y'] = 0

#Definição de um botão que vai sair do jogo
botao_sair = botao_iniciar_jogo.copy()
botao_sair['id'] = 'btnSair'
botao_sair['x'] = 0
botao_sair['y'] = -60

#Definição de um botão de instruções
botao_instrucoes = botao_iniciar_jogo.copy()
botao_instrucoes['id'] = 'btnInstrucoes'
botao_instrucoes['x'] = 0
botao_instrucoes['y'] = 60