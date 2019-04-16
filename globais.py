from OpenGL.GLUT import *
import time
glutInit()
start = time.time()
c = 1
esta_pausado = False
distancia_permitida = 22 #Distancia permitida entre quadaddos
quadrado = {
    'id': 0 , #int
    'x': 0, #float
    'y': 0, #float
    'largura': 0, #float
    'altura': 0, #float
    'visivel':True, #booleano
    'velocidade': 0, #float/int
    'area': 0, #float
    'n_colisoes': 0,
    'cor': (0, 0, 0)
}
anzol = quadrado.copy()
backg_e = {'x':0,'y':0,'altura':200,'larg':200,'cor':1}
backg_d = {'x':0,'y':0,'altura':1000,'larg':200,'cor':1}
PTS = 0
#Definindo o meu anzol
anzol['x'] = 20
anzol['y'] = 90
anzol['altura'] = 8
anzol['largura'] = 8
anzol['velocidade'] = 3
anzol['area'] = anzol['altura']**2
anzol['cor'] = (1, 1, 1)


