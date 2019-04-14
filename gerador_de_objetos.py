from globais import *
from random import randint
def analise_de_proximidade(x_object, y_object, lista_objetos):
    for c in lista_objetos:
        distancia = ((x_object - c['x'])**2 + (y_object - c['y'])**2)**0.5
        if distancia < 15:
            return True
    return False


def gerador_objetos(altura, largura, velocidade, quantidade):
    lista_objetos = []
    for c in range(quantidade):
        objeto = quadrado.copy()
        x_object = randint(-95, 95)
        y_object = randint(-95, -20)
        while analise_de_proximidade(x_object, y_object, lista_objetos):
            x_object = randint(-95, 95)
            y_object = randint(-95, -65)
        # Definindo a lista de objetos
        objeto['x'] = x_object
        objeto['y'] = y_object
        objeto['altura'] = altura
        objeto['largura'] = largura
        objeto['velocidade'] = velocidade
        objeto['area'] = objeto['altura']*objeto['largura']
        lista_objetos.append(objeto.copy())
    return lista_objetos