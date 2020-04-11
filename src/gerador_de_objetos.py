from src.globais import *
from random import randint
def gerador_objetos(id, altura, largura, velocidade, quantidade, cor):
    lista_objetos = []
    objeto = quadrado.copy()
    for c in range(quantidade):
        objeto['altura'] = altura
        objeto['largura'] = largura
        objeto['velocidade'] = velocidade
        objeto['area'] = objeto['altura']*objeto['largura']
        objeto['cor'] = cor
        objeto['direcao'] = randint(0, 2)
        objeto['id'] = id
        lista_objetos.append(objeto.copy())
    return lista_objetos