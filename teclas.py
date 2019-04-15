from globais import *
from OpenGL.GLUT import *

def tecla(key, x = 0, y = 0):
    global start
    tec = ord(key)
    if tec == 27: #ESC
        end = time.time()
        print(end - start)
        exit()
    elif tec == 114: #r
        print('reiniciando o programa')
    elif tec == 112: #p
        print('Pausando o programa')
    if tec == 115: #baixo (s)
        anzol['y'] -= anzol['velocidade']
    elif tec == 119: #cima (w)
        anzol['y'] += anzol['velocidade']
    elif tec == 97: #esquerda (a)
        anzol['x'] -= anzol['velocidade']
    elif tec == 100: #direita (d)
        anzol['x'] += anzol['velocidade']
    glutPostRedisplay()

def movimenta_anzol(self, key, x = 0, y = 0):
    if self == GLUT_KEY_DOWN and anzol['y'] >= -95: #seta baixo
        anzol['y'] -= anzol['velocidade']
    elif self == GLUT_KEY_UP and anzol['y'] <= 95: #seta cima
        anzol['y'] += anzol['velocidade']
    elif self == GLUT_KEY_LEFT and anzol['x'] >= -95: #seta esquerda
        anzol['x'] -= anzol['velocidade']
    elif self == GLUT_KEY_RIGHT and anzol['x'] <= 95: #seta direita
        anzol['x'] += anzol['velocidade']
    glutPostRedisplay()