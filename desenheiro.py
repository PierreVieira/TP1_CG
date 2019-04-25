from basico import *
from globais import *
from deslocamento1 import *
from deslocamento2 import *
from deslocamento3 import *
from objetos_terceira_parte import*
from colisao import collision
from OpenGL.GLUT import *
from OpenGL.GL import *
import menu_pause
import texturas
import menu_confi
import txt

def ninja_rand():
    t = time() - globais.start
    if t - globais.aux_t_ninjas >= 5:
        r = randint(0, 3)
        if r == 0:
            texturas.init_tex(globais.imgload[42], globais.img[42])
            globais.aux_rand_ninja = 0
        elif r == 1:
            texturas.init_tex(globais.imgload[43], globais.img[43])
            globais.aux_rand_ninja = 1
        else:
            texturas.init_tex(globais.imgload[44], globais.img[44])
            globais.aux_rand_ninja = 2
        globais.aux_t_ninjas = t
    else:
        if globais.aux_rand_ninja == 0:
            texturas.init_tex(globais.imgload[42], globais.img[42])
        elif globais.aux_rand_ninja == 1:
            texturas.init_tex(globais.imgload[43], globais.img[43])
        elif globais.aux_rand_ninja == 2:
            texturas.init_tex(globais.imgload[44], globais.img[44])

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
    k = 2
    altura = k*largura
    glViewport(GLint(0), GLint(0), int(altura/2), int(altura/2))

def desenha_quadrado(quadrado, i=0):
    glBegin(GL_POLYGON)
    if (quadrado['id'] != 30 or globais.parte != 2) and globais.parte != 'tela_inicial':
        glColor3f(1, 1, 1)
    else:
        glColor3f(quadrado['cor'][0], quadrado['cor'][1], quadrado['cor'][2])
    glTexCoord(0+i, 0)
    glVertex2f(quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2)
    glTexCoord(1-i, 0)
    glVertex2f(quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2)
    glTexCoord(1-i, 1)
    glVertex2f(quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2)
    glTexCoord(0+i, 1)
    glVertex2f(quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2)
    glEnd()

def redesenha():
    glClear(GL_COLOR_BUFFER_BIT)
    #glClearColor(0, 0.5, 1, 1)  #Fundo
    t = time() - globais.start
    if globais.parte == 'tela_inicial':
        texturas.init_tex(globais.imgload[35], globais.img[35])
        if globais.tela_i['cor'][0] < 1 and globais.tela_i['cor'][1] < 1 and globais.tela_i['cor'][2] < 1:
            globais.tela_i['cor'][0] = t/5
            globais.tela_i['cor'][1] = t/5
            globais.tela_i['cor'][2] = t/5
        if t > 3.5:
            globais.parte = 'menu'
        desenha_quadrado(globais.tela_i)
        glutSwapBuffers()
    elif globais.parte == 'menu':
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
        texturas.init_tex(globais.imgload[50], globais.img[50])
        desenha_quadrado(globais.botao_borda)
        #texturas.init_tex('seguidor_mouse')
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()
    elif globais.parte == 'instrucoes':
        texturas.init_tex(globais.imgload[34], globais.img[34])
        desenha_quadrado(globais.tela_instrucoes)
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()
    elif globais.parte == 'ranking':
        texturas.init_tex(globais.imgload[29], globais.img[29])
        desenha_quadrado(globais.tela_ranking)
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()
    elif globais.parte == 'creditos':
        texturas.init_tex(globais.imgload[31], globais.img[31])
        desenha_quadrado(globais.tela_creditos)
        desenha_quadrado(globais.seguidor_mouse)
        glutSwapBuffers()

    elif globais.parte == 1:
        texturas.init_tex(globais.imgload[2], globais.img[2])
        desenha_quadrado(backg)
        texturas.init_tex(globais.imgload[16], globais.img[16])
        desenha_quadrado(anzol)
        texturas.init_tex(globais.imgload[18], globais.img[18])
        for c in PTS:
            txt.Pts(c['id'])
            desenha_quadrado(c)
        if all1[-1]['id'] == 3 and globais.esta_pausado:
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        texturas.init_tex(globais.imgload[14], globais.img[14])
                    elif c['id'] == 1:
                        texturas.init_tex(globais.imgload[40], globais.img[40])
                    elif c['id'] == 2:
                        texturas.init_tex(globais.imgload[64], globais.img[64])
                    elif c['id'] == 3:
                        texturas.init_tex(globais.imgload[32], globais.img[32])
                        deslocar(True)
                    desenha_quadrado(c)
                    collision(anzol, c)
            if globais.esta_querendo_confirmar:
                texturas.init_tex(globais.imgload[47], globais.img[47])
                desenha_quadrado(menu_confi.mc)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        elif globais.esta_pausado:
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        alterna_lolis(0, 1)
                    elif c['id'] == 1:
                        alterna_lolis(38, 39)
                    elif c['id'] == 2:
                        alterna_lolis(66, 67)
                    desenha_quadrado(c)
                    menu_pause.menu_p()
            if globais.esta_querendo_confirmar:
                texturas.init_tex(globais.imgload[47], globais.img[47])
                desenha_quadrado(menu_confi.mc)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        else:
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
                        alterna_lolis(38, 39)
                    elif c['id'] == 2:
                        alterna_lolis(66, 67)
                    desenha_quadrado(c)
                    deslocar(False)
                    collision(anzol, c)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()

    elif globais.parte == 2:
        for c in range(len(all1)):
            if all1[c]['id'] == 'loli_vida':
                all1[c]['altura'] = 20
                all1[c]['largura'] = 20
            else:
                all1[c]['altura'] = 11
                all1[c]['largura'] = 11

        globais.anzol['velocidade'] = 12
        if globais.pts > 600:
            cor_back()
        texturas.init_tex(globais.imgload[37], globais.img[37])
        desenha_quadrado(backg)
        texturas.init_tex(globais.imgload[16], globais.img[16])
        desenha_quadrado(anzol)
        texturas.init_tex(globais.imgload[18], globais.img[18])
        for c in PTS:
            txt.Pts(c['id'])
            desenha_quadrado(c)

        # if globais.esta_pausado and globais.estou_em_transicao:
        #     for c in all2:
        #         texturas.init_tex(globais.imgload[0], globais.img[0])
        #         if c['id'] == 4:
        #             desenha_quadrado(c)
        #     texturas.init_tex(globais.imgload[48], globais.img[48])
        #     trans2()
        #     glutSwapBuffers()
        if globais.esta_pausado:
            for c in shots:
                if c['visivel']:
                    glPushMatrix()
                    glRotatef(c['x']/3, 0, 0, 1)
                    texturas.init_tex(globais.imgload[70], globais.img[70])
                    desenha_quadrado(c)
                    collision(anzol, c)
                    glPopMatrix()
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        texturas.init_tex(globais.imgload[15], globais.img[15])
                    elif c['id'] == 1:
                        texturas.init_tex(globais.imgload[41], globais.img[41])
                    elif c['id'] == 2:
                        texturas.init_tex(globais.imgload[65], globais.img[65])
                    elif c['id'] == 'loli_vida':
                        texturas.init_tex(globais.imgload[36], globais.img[36])
                    desenha_quadrado(c)
            for c in all2:
                if c['visivel']:
                    if c['id'] == 4:
                        texturas.init_tex(globais.imgload[71], globais.img[71])
                    else:
                        texturas.init_tex(globais.imgload[69], globais.img[69])
                    desenha_quadrado(c)
                    collision(anzol, c)
            for c in lives:
                texturas.init_tex(globais.imgload[28], globais.img[28])
                desenha_quadrado(c)
            menu_pause.menu_p()
            if globais.esta_querendo_confirmar:
                texturas.init_tex(globais.imgload[47], globais.img[47])
                desenha_quadrado(menu_confi.mc)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
        elif not(globais.esta_pausado):
            for c in shots:
                if c['visivel']:
                    glPushMatrix()
                    glRotatef(c['x']/3, 0, 0, 1)
                    texturas.init_tex(globais.imgload[70], globais.img[70])
                    desenha_quadrado(c)
                    move()
                    collision(anzol, c)
                    glPopMatrix()
            for c in all1:
                if c['visivel']:
                    if c['id'] == 0:
                        texturas.init_tex(globais.imgload[15], globais.img[15])
                    elif c['id'] == 1:
                        texturas.init_tex(globais.imgload[41], globais.img[41])
                    elif c['id'] == 2:
                        texturas.init_tex(globais.imgload[65], globais.img[65])
                    elif c['id'] == 'loli_vida':
                        texturas.init_tex(globais.imgload[36], globais.img[36])
                    padrao_2(c)
            for c in all2:
                if c['visivel']:
                    if c['id'] == 4:
                        texturas.init_tex(globais.imgload[71], globais.img[71])
                    else:
                        texturas.init_tex(globais.imgload[69], globais.img[69])
                    padrao_2(c)
            for c in lives:
                texturas.init_tex(globais.imgload[28], globais.img[28])
                desenha_quadrado(c)
            desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()

    elif globais.parte == 3:
        texturas.init_tex(globais.imgload[68], globais.img[68])
        desenha_quadrado(backg2)
        texturas.init_tex(globais.imgload[16], globais.img[16])
        desenha_quadrado(anzol)
        texturas.init_tex(globais.imgload[18], globais.img[18])
        for c in PTS:
            txt.Pts(c['id'])
            desenha_quadrado(c)
        if not(globais.esta_pausado):
            for c in ninjas:
                if c['visivel']:
                    if c['id'] == 130:
                        texturas.init_tex(globais.imgload[52], globais.img[52])
                    elif c['id'] == 120:
                        texturas.init_tex(globais.imgload[51], globais.img[51])
                    elif collision(anzol, c):
                        texturas.init_tex(globais.imgload[45], globais.img[45])
                    else:
                        ninja_rand()
                    if c['x'] >= 0:
                        desenha_quadrado(c, 1)
                    else:
                        desenha_quadrado(c)
                    mov_ninjas()
                    collision(seguidor_mouse, c)
                else:
                    verificar_tempo(c)
                    desenha_quadrado(seguidor_mouse)
            for c in lives:
                texturas.init_tex(globais.imgload[28], globais.img[28])
                desenha_quadrado(c)
            glutSwapBuffers()
        elif globais.esta_pausado:
            for c in ninjas:
                if c['visivel']:
                    if c['id'] == 130:
                        texturas.init_tex(globais.imgload[52], globais.img[52])
                    elif c['id'] == 120:
                        texturas.init_tex(globais.imgload[51], globais.img[51])
                    elif collision(anzol, c):
                        texturas.init_tex(globais.imgload[45], globais.img[45])
                    else:
                        ninja_rand()
                    if globais.anzol['x'] <= 0:
                        desenha_quadrado(c, 1)
                    else:
                        desenha_quadrado(c)
                        collision(globais.anzol, c)
                    for c in lives:
                        texturas.init_tex(globais.imgload[28], globais.img[28])
                        desenha_quadrado(c)
                    menu_pause.menu_p()
                    if globais.esta_querendo_confirmar:
                        texturas.init_tex(globais.imgload[47], globais.img[47])
                        desenha_quadrado(menu_confi.mc)
                    desenha_quadrado(globais.seguidor_mouse)
            glutSwapBuffers()
    elif globais.parte == 'game_over':
        texturas.init_tex(globais.imgload[63], globais.img[63])
        desenha_quadrado(globais.game_over)
        glutSwapBuffers()
