from OpenGL.GLUT import *
import time
aux_musica = True
glutInit()
aux_t_col = 0
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
seguidor_mouse['largura'] = 2
seguidor_mouse['altura'] = 2


#Definindo um quadrado para as telas
tela_inicial = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (0, 0, 0)}
tela_creditos = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (0, 0, 1)}
tela_instrucoes = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (1, 0, 1)}
tela_ranking = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (0, 1, 0)}

#Definição de fundos
backg_e = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': (0, 0, 0)}
backg_d = {'x': 0, 'y': 0, 'altura': 1000, 'largura': 200, 'cor': (0, 0, 0)}


#Variável global para pontuação
PTS = 0

#Definindo o meu anzol
anzol = quadrado.copy()
anzol['x'] = 20
anzol['y'] = 90
anzol['altura'] = 8
anzol['visivel'] = True
anzol['largura'] = 8
anzol['velocidade'] = 8
anzol['area'] = anzol['altura']**2
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
botao_creditos['y'] = -90

#Definição de um botão que vai para a tela de fases
botao_fases = botao_iniciar_jogo.copy()
botao_fases['id'] = 'btnFases'
botao_fases['x'] = -70
botao_fases['y'] = 0

#Definição de um botão que vai acessa o ranking
botao_ranking = botao_iniciar_jogo.copy()
botao_ranking['id'] = 'btnRanking'
botao_ranking['x'] = 70
botao_ranking['y'] = 0

#Definição de um botão que vai sair do jogo
botao_sair = botao_iniciar_jogo.copy()
botao_sair['id'] = 'btnSair'
botao_sair['x'] = 70
botao_sair['y'] = -90

#Definição de um botão de instruções
botao_instrucoes = botao_iniciar_jogo.copy()
botao_instrucoes['id'] = 'btnInstrucoes'
botao_instrucoes['x'] = 0
botao_instrucoes['y'] = 60