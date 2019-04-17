from random import randint
from globais import *
def analise_de_proximidade(x_object, y_object, lista_objetos):
    for c in lista_objetos:
        distancia = ((x_object - c['x'])**2 + (y_object - c['y'])**2)**0.5
        if distancia < distancia_permitida:
            return True
    return False

def gerador_objetos1(lista_peixes):
    todos_objetos = []
    all_objects = []
    for c in lista_peixes:
        for d in c:
            todos_objetos.append(d)
    for c in todos_objetos:
        x_object = randint(-95, 95)
        y_object = randint(-95, 0)
        while analise_de_proximidade(x_object, y_object, todos_objetos):
            x_object = randint(-95, 95)
            y_object = randint(-95, -35)
        # Definindo a lista de objetos
        c['x'] = x_object
        c['y'] = y_object
        all_objects.append(c)
    return all_objects