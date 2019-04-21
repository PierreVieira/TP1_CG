from OpenGL import GL
import menu_confi
from basico import *
from globais import *
from objetos_segunda_parte import *
from deslocamento1 import *
from deslocamento2 import *
from colisao import collision
from OpenGL.GLUT import *
from OpenGL.GL import *
#from sdl2 import *
import menu_pause
# def LoadTexture(self, filename):
#     """Loads a texture for the cube"""
#     surface = SDL_LoadBMP(filename)
#     #Checks if the loading succeeded
#     if surface:
#         #Translate the LP_SDL_Surface-pointer got from SDL_LoadBMP() to a real SDL_Surface
#         texture_surface = surface.contents
#         texture_format = GL.GL_RGBA
#         GL_TEXTURE_ID = GL.glGenTextures(1)
#         GL.glBindTexture(GL.GL_TEXTURE_2D, GL_TEXTURE_ID)
#         GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
#         GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, 3, texture_surface.w, texture_surface.h, 0, texture_format, GL.GL_UNSIGNED_BYTE, texture_surface)
#         return GL_TEXTURE_ID
#     return None

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
    #glEnable(GL_TEXTURE_2D)
    #glBindTexture(GL_TEXTURE_2D, idTextura)
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
    if globais.parte == 'menu':
        desenha_quadrado(globais.tela_inicial)
        desenha_quadrado(globais.botao_iniciar_jogo)
        desenha_quadrado(globais.botao_creditos)
        desenha_quadrado(globais.botao_fases)
        desenha_quadrado(globais.botao_ranking)
        desenha_quadrado(globais.botao_sair)
        desenha_quadrado(globais.botao_instrucoes)
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()
    elif globais.parte == 'instrucoes':
        desenha_quadrado(globais.tela_instrucoes)
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()
    elif globais.parte == 'ranking':
        desenha_quadrado(globais.tela_ranking)
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()
    elif globais.parte == 'creditos':
        desenha_quadrado(globais.tela_creditos)
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()
    elif globais.parte == 1:
        if all1[-1]['id'] == 3 and globais.esta_pausado:
            desenha_quadrado(anzol)
            for c in all1:
                if c['visivel']:
                    desenha_quadrado(c)
                    if c['id'] == 3:
                        deslocar(True)
                    collision(anzol, c)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        elif globais.esta_pausado:
            desenha_quadrado(anzol)
            for c in all1:
                if c['visivel']:
                    desenha_quadrado(c)
                    menu_pause.menu_p()
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        else:
            desenha_quadrado(anzol)
            #pts(GLUT_BITMAP_TIMES_ROMAN_24,PTS.str().zfill(5),50,45,0)
            for c in all1:
                if c['visivel']:
                    desenha_quadrado(c)
                    deslocar(False)
                    collision(anzol, c)
            desenha_quadrado(globais.seguidor_mouse)
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
                    glPushMatrix()
                    glRotatef(c['x']/3, 0, 0, 1)
                    desenha_quadrado(c)
                    move()
                    collision(anzol, c)
                    glPopMatrix()
            for c in all1:
                if c['visivel']:
                    padrao_2(c)
            for c in all2:
                if c['visivel']:
                    padrao_2(c)
            glutSwapBuffers()
