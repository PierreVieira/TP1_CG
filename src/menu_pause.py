from src import desenheiro, globais, texturas

#Definindo um quadrado para o submenu
mp = globais.quadrado.copy()
mp['largura'] = 50
mp['altura'] = 100
mp['cor'] = (1, 0, 0)

#Definição de botões no menu de pause
voltar_menu_principal = globais.quadrado.copy()
voltar_menu_principal['largura'] = 30
voltar_menu_principal['altura'] = 20
voltar_menu_principal['y'] = 30
voltar_menu_principal['cor'] = (0, 1, 0)
voltar_menu_principal['id'] = 'btnVoltarMenuPrincipal'

#Definindo um botão para deixar o audio mudo
audio_switchE = voltar_menu_principal.copy()
audio_switchE['largura'] = 15
audio_switchE['x'] = -8
audio_switchE['y'] = 0
audio_switchE['id'] = 'btnAudio_switchE'

#Definindo um botão para deixar o audio_com_som
audio_switchD = voltar_menu_principal.copy()
audio_switchD['largura'] = 15
audio_switchD['x'] = 8
audio_switchD['y'] = 0
audio_switchD['id'] = 'btnAudio_switchD'

#Definindo um botão quitar o game
quitar_game = voltar_menu_principal.copy()
quitar_game['y'] = -30
quitar_game['id'] = 'btnQuitar_game'

def menu_p():
    if not(globais.estou_em_transicao):
        texturas.init_tex(globais.imgload[9], globais.img[9])
        desenheiro.desenha_quadrado(mp)
        texturas.init_tex(globais.imgload[10], globais.img[10])
        desenheiro.desenha_quadrado(voltar_menu_principal)
        texturas.init_tex(globais.imgload[11], globais.img[11])
        desenheiro.desenha_quadrado(audio_switchE)
        texturas.init_tex(globais.imgload[12], globais.img[12])
        desenheiro.desenha_quadrado(audio_switchD)
        texturas.init_tex(globais.imgload[13], globais.img[13])
        desenheiro.desenha_quadrado(quitar_game)