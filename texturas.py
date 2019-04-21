from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame
def init_tex(t_id):
    if t_id == 'anzol':
        nome_textura = 'Os trem/Edge.png'
    elif t_id == 0:
        nome_textura = 'Os trem/loli_1.png'
    elif t_id == 'backg':
        nome_textura = 'Os trem/Tokyo.png'
    else:
        nome_textura = 'Os trem/loli_1.png'

    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_MODELVIEW)
    texture_ids = glGenTextures(1)
    imgload = pygame.image.load(nome_textura)
    img = pygame.image.tostring(imgload, 'RGBA', 1)
    largura = imgload.get_width()
    altura = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture_ids)

    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, largura, altura, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)
    glEnable(GL_TEXTURE_2D)