from basico import *
from globais import *
from peixes_e_traps import *
from colisao import collision
from OpenGL.GLUT import *
from OpenGL.GL import *

def manter_prop(largura, altura):
    k = 4/3
    # altura = 4
    # largura = 3
    altura = k*largura
    #glViewport(GLint(0), GLint(0), int(altura/2), int(altura/2))

def desenha_quadrado(quadrado, cor):
    glBegin(GL_POLYGON)
    glColor3f(cor[0], cor[1], cor[2])
    glVertex2f(quadrado['x'] - quadrado['largura']/2, quadrado['y'] - quadrado['altura']/2)
    glVertex2f(quadrado['x'] + quadrado['largura']/2, quadrado['y'] - quadrado['altura']/2)
    glVertex2f(quadrado['x'] + quadrado['largura']/2, quadrado['y'] + quadrado['altura']/2)
    glVertex2f(quadrado['x'] - quadrado['largura']/2, quadrado['y'] + quadrado['altura']/2)
    glEnd()

def redesenha():
    glClearColor(0, 0.5, 1, 1)  #Fundo
    glClear(GL_COLOR_BUFFER_BIT)
    desenha_quadrado(anzol, (1, 1, 1))
    #pts(GLUT_BITMAP_TIMES_ROMAN_24,PTS.str().zfill(5),50,45,0)
    for c in lista_peixes:
        for d in c:
            desenha_quadrado(d, (1, 1, 0))
            collision(anzol, d)
    glutSwapBuffers()