from basico import *
from globais import *
from objetos_segunda_parte import *
from deslocamento1 import *
from deslocamento2 import *
from colisao import collision
from OpenGL.GLUT import *
from OpenGL.GL import *
import menu_pause

def padrao_2(c):
    desenha_quadrado(c)
    move()
    collision(anzol, c)

def manter_prop(largura, altura):
    k = 4/3
    altura = 4
    largura = 3
    altura = k*largura
    glViewport(GLint(0), GLint(0), int(altura/2), int(altura/2))

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
    if globais.parte == 1:
        if all1[-1]['id'] == 3 and globais.esta_pausado:
            desenha_quadrado(anzol)
            for c in all1:
                if c['visivel']:
                    desenha_quadrado(c)
                    if c['id'] == 3:
                        deslocar(True)
                    collision(anzol, c)
            glutSwapBuffers()
        elif globais.esta_pausado:
            desenha_quadrado(anzol)
            for c in all1:
                if c['visivel']:
                    desenha_quadrado(c)
                    menu_pause.menu_p()
            glutSwapBuffers()
        else:
            desenha_quadrado(anzol)
            #pts(GLUT_BITMAP_TIMES_ROMAN_24,PTS.str().zfill(5),50,45,0)
            for c in all1:
                if c['visivel']:
                    desenha_quadrado(c)
                    deslocar(False)
                    collision(anzol, c)
            glutSwapBuffers()

    elif globais.parte == 2:
        globais.anzol['velocidade'] = 12
        if globais.esta_pausado:
            desenha_quadrado(anzol)
            for c in all1:
                if c['visivel']:
                    desenha_quadrado(c)
            for c in all2:
                if c['visivel']:
                    desenha_quadrado(c)
                    collision(anzol, c)
            menu_pause.menu_p()
            glutSwapBuffers()
        else:
            desenha_quadrado(anzol)
            for c in shots:
                if c['visivel']:
                    padrao_2(c)
            for c in all1:
                if c['visivel']:
                    padrao_2(c)
            for c in all2:
                if c['visivel']:
                    padrao_2(c)
            glutSwapBuffers()
