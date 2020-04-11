from pygame import mixer
from src import globais


def padraozinhoPlayzim(nome_arq):
    mixer.music.load(nome_arq)
    mixer.music.play()
    globais.aux_musica = False

def tocarMusica():
    mixer.init()
    if globais.parte == 1 and globais.aux_musica:
        padraozinhoPlayzim('images/Senbonzakura.mp3')
    elif globais.parte == 2 and globais.aux_musica:
        padraozinhoPlayzim('images/Adestrador De Madeon.mp3')
    elif globais.parte == 'creditos' and globais.aux_musica:
        padraozinhoPlayzim('images/dbs_YokaYoka Dance.mp3')
    elif globais.parte == 'menu' and globais.aux_musica:
       padraozinhoPlayzim('images/Dark Souls III Soundtrack OST - Main Menu Theme.mp3')
    elif globais.parte == 3 and globais.aux_musica:
       padraozinhoPlayzim('images/DBS.mp3')