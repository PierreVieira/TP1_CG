import globais
from OpenGL.GLUT import *
def atual(time):
    if not(globais.esta_pausado):
        glutPostRedisplay()
    # print(globais.esta_pausado)
    glutTimerFunc(33, atual, 33)
