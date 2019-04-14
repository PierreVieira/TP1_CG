from desenheiro import *
#from atualizar import *
from teclas import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def main_basico():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(500, 100)
    glutCreateWindow(b'Pescaria')
    glutDisplayFunc(redesenha)
    glutReshapeFunc(manter_prop)
    glOrtho(-100, 100, -100, 100, -1, 1)
    glutKeyboardFunc(tecla)
    glutSpecialFunc(movimenta_anzol)
 #   glutTimerFunc(33, atualiza, 33)
    glutMainLoop()
