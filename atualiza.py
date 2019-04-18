from OpenGL.GLUT import *

def atual(time):
    glutPostRedisplay()
    glutTimerFunc(33, atual, 33)
