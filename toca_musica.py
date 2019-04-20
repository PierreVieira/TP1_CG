from pygame import mixer
import globais

def padraozinhoPlayzim(nome_arq):
    mixer.music.load(nome_arq)
    mixer.music.play()
    globais.aux_musica = False

def tocarMusica():
    mixer.init()
    if globais.parte == 1 and globais.aux_musica:
        padraozinhoPlayzim('Senbonzakura.mp3')
    elif globais.parte == 2 and globais.aux_musica:
        mixer.music.load('Senbonzakura.mp3')
        mixer.music.play()
        globais.aux_musica = False
    elif globais.parte == 'creditos' and globais.aux_musica:
        padraozinhoPlayzim('dbs_YokaYoka Dance.mp3')
    elif globais.parte == 'menu' and globais.aux_musica:
        mixer.music.load('Naruto.mp3')
        mixer.music.play()
        globais.aux_musica = False
