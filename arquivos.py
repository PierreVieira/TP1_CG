#Manipulando arquivos em python
from datetime import datetime
def exibir_resultado():
    manipulador3 = open('hs.txt', 'r')
    lista = manipulador3.readlines()
    print('\033[1;31;0m====== ESTES SÃO OS MELHORES JOGADORES ======\n\033[m')
    for c in lista:
        print(f'\033[0;34;0m{c}\n\033[m',end='')
    print('\033[1;31;0m=============================================\n\033[m')

def alteracao_data(colocacao):
    atual = datetime.now()
    lista_atuais = [atual.day, atual.month, atual.year, atual.hour, atual.minute, atual.second]
    s = str(colocacao)+'°: '
    for c in range(3):
        if c < 3:
            s += str(lista_atuais[c])
            if c != 2:
                s +='/'
    s += ' | '
    for c in range(3):
        s += str(lista_atuais[c+3])
        if c != 2:
            s += ':'
    s += '\n'
    alterador = open('datas_hs.txt', 'w')
    print(s)

def alterar(lista_pontuacao2, nome, pontuacao, colocacao):
    manipulador2 = open('hs.txt', 'w')
    lista_pontuacao2[colocacao - 1][1] = nome
    lista_pontuacao2[colocacao - 1][3] = pontuacao
    for c in lista_pontuacao2:
        s = ''
        for d in c:
            s += d+' '
        manipulador2.write(s+'\n')
    manipulador2.close()
    alteracao_data(colocacao)
    exibir_resultado()

def hank(nomeJogador, pontuacaoJogador):
    manipulador = open('hs.txt', 'r')
    lista_pontuacao = manipulador.readlines()
    manipulador.close() #fecha o arquivo
    lista_pontuacao2 = []
    lista_pontuacao3 = []
    for c in lista_pontuacao:
        lista_pontuacao2.append(c.split())
    for c in lista_pontuacao2:
        for d in range(len(c)):
            if d == 3:
                lista_pontuacao3.append(c[d])

    if pontuacaoJogador > int(lista_pontuacao3[0]):
        alterar(lista_pontuacao2 ,nomeJogador, str(pontuacaoJogador), 1)
    elif pontuacaoJogador > int(lista_pontuacao3[1]):
        alterar(lista_pontuacao2 ,nomeJogador, str(pontuacaoJogador), 2)
    elif pontuacaoJogador > int(lista_pontuacao3[2]):
        alterar(lista_pontuacao2 ,nomeJogador, str(pontuacaoJogador), 3)
    elif pontuacaoJogador > int(lista_pontuacao3[3]):
        alterar(lista_pontuacao2 ,nomeJogador, str(pontuacaoJogador), 4)
    elif pontuacaoJogador > int(lista_pontuacao3[4]):
        alterar(lista_pontuacao2 ,nomeJogador, str(pontuacaoJogador), 5)

hank(input().split()[0], int(input()))