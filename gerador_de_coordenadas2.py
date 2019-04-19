from random import randint
from objetos_segunda_parte import *

def analise_de_proximidade(x_object, y_object, lista_objetos, distancia_permitida):
    for c in lista_objetos:
        distancia = ((x_object - c['x'])**2 + (y_object - c['y'])**2)**0.5
        if distancia < distancia_permitida:
            return True
    return False

def gerador_objetos2(lista_traps):
    for c in lista_traps:
        for d in range(len(c)):
            if d <= 4:
                if randint(0,2) == 1:
                    x = randint(12, 16)
                else:
                    x = randint(-16, -12)
                y = randint(-95, -47)
                while analise_de_proximidade(x, y, c, 10):
                    if randint(0, 2) == 1:
                        x = randint(12, 16)
                    else:
                        x = randint(-16, -12)
                    y = randint(-95, -47)
                c[d]['x'] = x
                c[d]['y'] = y

    return c
