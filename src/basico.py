from src.desenheiro import *
from src.atualiza import *
from src.teclas import *
from src.mouse import *
def main_basico():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 700)
    glutInitWindowPosition(500, 100)
    glutCreateWindow(b'Loli Fishing')
    glutDisplayFunc(redesenha)
    #glutReshapeFunc(manter_prop)
    glOrtho(-100, 100, -100, 100, -1, 1)
    glutKeyboardFunc(tecla)
    glutSpecialFunc(movimenta_anzol)
    glutPassiveMotionFunc(movimentoMouse)
    glutMouseFunc(clicks_do_mouse)
    glutTimerFunc(33, atual, 33)
    glutMainLoop()
