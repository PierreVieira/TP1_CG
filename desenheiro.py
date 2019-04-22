from basico import *
from globais import *
from deslocamento1 import *
from deslocamento2 import *
from colisao import collision
from OpenGL.GLUT import *
from OpenGL.GL import *
import menu_pause
import texturas
import menu_confi
import txt

def alterna_lolis(arq1,arq2):
    if globais.alterna_loli:
        texturas.init_tex(globais.imgload[arq1], globais.img[arq1])
    else:
        texturas.init_tex(globais.imgload[arq2], globais.img[arq2])

def pause_ambas():
    if globais.parte == 1:
        desenha_quadrado(anzol)
        for c in all1:
            if c['visivel']:
                desenha_quadrado(c)
        desenha_quadrado(globais.seguidor_mouse)
        menu_pause.menu_p()
        glutSwapBuffers()
    elif globais.parte == 2:
        desenha_quadrado(anzol)
        for c in shots:
            if c['visivel']:
                glPushMatrix()
                glRotatef(c['x'] / 3, 0, 0, 1)
                desenha_quadrado(c)
                collision(anzol, c)
                glPopMatrix()
        for c in all1:
            if c['visivel']:
                desenha_quadrado(c)
        for c in all2:
            if c['visivel']:
                desenha_quadrado(c)
                collision(anzol, c)
        menu_pause.menu_p()
        glutSwapBuffers()

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
    glColor3f(1, 1, 1)
    glTexCoord(0, 0)
    glVertex2f(quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2)
    glTexCoord(1, 0)
    glVertex2f(quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2)
    glTexCoord(1, 1)
    glVertex2f(quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2)
    glTexCoord(0, 1)
    glVertex2f(quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2)
    glEnd()

def redesenha():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0, 0.5, 1, 1)  #Fundo
    if globais.parte == 'menu':
        texturas.init_tex(globais.imgload[3], globais.img[3])
        desenha_quadrado(globais.tela_inicial)
        texturas.init_tex(globais.imgload[4], globais.img[4])
        desenha_quadrado(globais.botao_iniciar_jogo)
        texturas.init_tex(globais.imgload[8], globais.img[8])
        desenha_quadrado(globais.botao_creditos)
        texturas.init_tex(globais.imgload[5], globais.img[5])
        desenha_quadrado(globais.botao_ranking)
        texturas.init_tex(globais.imgload[6], globais.img[6])
        desenha_quadrado(globais.botao_sair)
        texturas.init_tex(globais.imgload[7], globais.img[7])
        desenha_quadrado(globais.botao_instrucoes)
        #texturas.init_tex('seguidor_mouse')
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
        texturas.init_tex(globais.imgload[2], globais.img[2])
        desenha_quadrado(backg)
        texturas.init_tex(globais.imgload[16], globais.img[16])
        desenha_quadrado(anzol)
        if all1[-1]['id'] == 3 and globais.esta_pausado:
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        alterna_lolis(0, 1)
                    elif c['id'] == 1:
                        alterna_lolis(2, 3)
                    elif c['id'] == 2:
                        alterna_lolis(4, 5)
                    elif c['id'] == 3:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                        deslocar(True)
                    desenha_quadrado(c)
                    collision(anzol, c)
            if globais.esta_querendo_confirmar:
                desenha_quadrado(menu_confi.mc)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        elif globais.esta_pausado:
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        alterna_lolis(0, 1)
                    elif c['id'] == 1:
                        alterna_lolis(2, 3)
                    elif c['id'] == 2:
                        alterna_lolis(4, 5)
                    desenha_quadrado(c)
                    menu_pause.menu_p()
            if globais.esta_querendo_confirmar:
                desenha_quadrado(menu_confi.mc)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        else:
            for c in PTS:
                txt.Pts(c['id'])
                desenha_quadrado(c)
            t = time() - globais.start
            tempo = int(t - globais.start)
            if tempo % 1 == 0 and tempo != globais.aux_tempo_alternacao1:
                globais.alterna_loli = not (globais.alterna_loli)
            globais.aux_tempo_alternacao1 = tempo
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        alterna_lolis(0, 1)
                    elif c['id'] == 1:
                        alterna_lolis(2, 3)
                    elif c['id'] == 2:
                        alterna_lolis(4, 5)
                    desenha_quadrado(c)
                    deslocar(False)
                    collision(anzol, c)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()

    elif globais.parte == 2:
        globais.anzol['velocidade'] = 12
        texturas.init_tex(globais.imgload[2], globais.img[2])
        desenha_quadrado(backg)
        texturas.init_tex(globais.imgload[16], globais.img[16])
        desenha_quadrado(anzol)
        if globais.esta_pausado:
            for c in shots:
                if c['visivel']:
                    glPushMatrix()
                    glRotatef(c['x']/3, 0, 0, 1)
                    texturas.init_tex(globais.imgload[6], globais.img[6])
                    desenha_quadrado(c)
                    collision(anzol, c)
                    glPopMatrix()
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    elif c['id'] == 1:
                        texturas.init_tex(globais.imgload[2], globais.img[2])
                    elif c['id'] == 2:
                        texturas.init_tex(globais.imgload[3], globais.img[3])
                    desenha_quadrado(c)
            for c in all2:
                if c['visivel']:
                    if c['id'] == 0:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    elif c['id'] == 1:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    elif c['id'] == 2:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    desenha_quadrado(c)
                    collision(anzol, c)
            for c in lives:
                texturas.init_tex(globais.imgload[0], globais.img[0])
                desenha_quadrado(c)
            menu_pause.menu_p()
            if globais.esta_querendo_confirmar:
                desenha_quadrado(menu_confi.mc)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        else:
            desenha_quadrado(anzol)
            for c in shots:
                if c['visivel']:
                    glPushMatrix()
                    glRotatef(c['x']/3, 0, 0, 1)
                    texturas.init_tex(globais.imgload[6], globais.img[6])
                    desenha_quadrado(c)
                    move()
                    collision(anzol, c)
                    glPopMatrix()
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    elif c['id'] == 1:
                        texturas.init_tex(globais.imgload[2], globais.img[2])
                    elif c['id'] == 2:
                        texturas.init_tex(globais.imgload[3], globais.img[3])
                    padrao_2(c)
            for c in all2:
                if c['visivel']:
                    if c['id'] == 0:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    elif c['id'] == 1:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    elif c['id'] == 2:
                        texturas.init_tex(globais.imgload[0], globais.img[0])
                    padrao_2(c)
            for c in lives:
                texturas.init_tex(globais.imgload[2], globais.img[2])
                desenha_quadrado(c)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
