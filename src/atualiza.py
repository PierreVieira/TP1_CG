from OpenGL.GLUT import *
from src.toca_musica import tocarMusica
def atual(time):
    glutPostRedisplay()
    tocarMusica()
    glutTimerFunc(33, atual, 33)
