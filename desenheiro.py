from basico import *
from globais import *
from objetos_segunda_parte import *
from objetos_primeira_parte import *
from deslocamento import *
from colisao import collision
from OpenGL.GLUT import *
from OpenGL.GL import *
from time import sleep

def manter_prop(largura, altura):
    k = 4/3
    # altura = 4
    # largura = 3
    altura = k*largura
    #glViewport(GLint(0), GLint(0), int(altura/2), int(altura/2))

def desenha_quadrado(quadrado):
    glBegin(GL_POLYGON)
    glColor3f(quadrado['cor'][0], quadrado['cor'][1], quadrado['cor'][2])
    glVertex2f(quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2)
    glVertex2f(quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2)
    glVertex2f(quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2)
    glVertex2f(quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2)
    glEnd()

def redesenha():
    glClearColor(0, 0.5, 1, 1)  #Fundo
    glClear(GL_COLOR_BUFFER_BIT)
    desenha_quadrado(anzol)
    #pts(GLUT_BITMAP_TIMES_ROMAN_24,PTS.str().zfill(5),50,45,0)
    for c in all1:
        deslocar()
        desenha_quadrado(c)
        collision(anzol, c)
    glutSwapBuffers()
    glutPostRedisplay()