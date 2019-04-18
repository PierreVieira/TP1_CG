from OpenGL.GLUT import *
from toca_musica import tocarMusica
def atual(time):
    tocarMusica()
    glutPostRedisplay()
    glutTimerFunc(33, atual, 33)
