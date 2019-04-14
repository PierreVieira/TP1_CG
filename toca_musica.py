from pygame import mixer
def tocarMusica():
    mixer.init()
    mixer.music.load('animals-martin-garrix-official-audio-hd.mp3')
    mixer.music.play()
