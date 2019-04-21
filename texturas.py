from OpenGL.GL import *
from OpenGL.GLUT import *
def init_tex(imgload, img):
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_MODELVIEW)
    texture_ids = glGenTextures(1)
    largura = imgload.get_width()
    altura = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture_ids)

    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, largura, altura, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)