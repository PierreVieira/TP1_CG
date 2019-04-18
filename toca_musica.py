from pygame import mixer
import globais
from time import time
def tocarMusica():
    if globais.parte == 1:
        nome_arquivo = 'Senbonzakura.mp3'
        tempo_arquivo = 190
    else:
        nome_arquivo = 'Sorteio.mp3'
        tempo_arquivo = 15
    if (time() - globais.start <= 1) or (int(time() - globais.start)%tempo_arquivo) == 0:
        mixer.init()
        mixer.music.load(nome_arquivo)
        mixer.music.play()

