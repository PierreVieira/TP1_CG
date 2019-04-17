from desenheiro import *
from atualiza import *
from teclas import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from globais import *

def main_basico():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(500, 100)
    glutCreateWindow(b'Pescaria')
    glutDisplayFunc(redesenha)
    #glutReshapeFunc(manter_prop)
    glOrtho(-100, 100, -100, 100, -1, 1)
    glutKeyboardFunc(tecla)
    glutSpecialFunc(movimenta_anzol)
    glutTimerFunc(33, atual, 33)
    glutMainLoop()
