from random import randint
from src import objetos_segunda_parte


def analise_de_proximidade(x_object, y_object, lista_objetos, distancia_permitida):
    for c in lista_objetos:
        distancia = ((x_object - c['x'])**2 + (y_object - c['y'])**2)**0.5
        if distancia < distancia_permitida:
            return True
    return False

def coord_tiro(lista_tiros):
    for c in lista_tiros:
        for d in range(len(c)):
            pos = randint(0, 5)
            c[d]['x'] = objetos_segunda_parte.all2[pos]['x']
            c[d]['y'] = objetos_segunda_parte.all2[pos]['y'] + 1
    return c

def coord_pts(lista_pts):
    for c in lista_pts:
        s = -100
        for d in range(len(c)):
            s += 6
            c[d]['x'] = s
            c[d]['y'] = 95
    return c

def coord_lives(lista_lives):
    for c in lista_lives:
        s = 100
        for d in range(len(c)):
            s -= 6
            c[d]['x'] = s
            c[d]['y'] = 95
    return c

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
