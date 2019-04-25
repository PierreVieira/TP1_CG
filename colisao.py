from objetos_primeira_parte import *
from deslocamento2 import *
from arquivos import *
import globais


def collision(objeto, quadrado):
    objV3 = objeto['x'] - objeto['largura'] / 2, objeto['y'] - objeto['altura'] / 2
    objV4 = objeto['x'] + objeto['largura'] / 2, objeto['y'] - objeto['altura'] / 2
    objV1 = objeto['x'] + objeto['largura'] / 2, objeto['y'] + objeto['altura'] / 2
    objV2 = objeto['x'] - objeto['largura'] / 2, objeto['y'] + objeto['altura'] / 2

    quadV3 = quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2
    quadV4 = quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2
    quadV1 = quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2
    quadV2 = quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2

    if quadV2[0] < objV3[0] < quadV1[0] and quadV4[1] < objV3[1] < quadV1[1] or \
            quadV2[0] < objV2[0] < quadV1[0] and quadV4[1] < objV2[1] < quadV1[1] or \
            quadV2[0] < objV1[0] < quadV1[0] and quadV4[1] < objV1[1] < quadV1[1] or \
            quadV2[0] < objV4[0] < quadV1[0] and quadV4[1] < objV4[1] < quadV1[1] or \
            \
            objV2[0] < quadV3[0] < objV1[0] and objV4[1] < quadV3[1] < objV1[1] or \
            objV2[0] < quadV2[0] < objV1[0] and objV4[1] < quadV2[1] < objV1[1] or \
            objV2[0] < quadV1[0] < objV1[0] and objV4[1] < quadV1[1] < objV1[1] or \
            objV2[0] < quadV4[0] < objV1[0] and objV4[1] < quadV4[1] < objV1[1]:
        objeto['n_colisoes'] += 1
        if globais.parte == 1 and objeto['id'] == 'anzol':
            quadrado['visivel'] = False
            globais.estou_em_transicao = True
            globais.esta_pausado = True
            camburao = globais.quadrado.copy()
            camburao['cor'] = (0.5, 0.5, 0.5)
            camburao['altura'] = 48
            camburao['largura'] = 24
            camburao['y'] = -125
            camburao['velocidade'] = 1
            camburao['id'] = 3
            all1.append(camburao)
        elif globais.parte == 2 and objeto['id'] == 'anzol':
            quadrado['visivel'] = False
            if quadrado['id'] == 'loli_vida':
                globais.pts += 50
                if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                    hank(globais.nomeJogador, globais.pts)
                    globais.parte = 'game_over'
                    return True
                vida['x'] = objetos_segunda_parte.lives[-1]['x'] - 6
                objetos_segunda_parte.lives.append(vida.copy())
            elif 0 <= quadrado['id'] <= 2:
                globais.pts += 10

            if globais.pts >= 100:
                globais.aux_musica = True
                sleep(1)
                globais.parte = 3
                return True

            elif quadrado['id'] == 4:
                if len(qtde_vidas[0]) <= 2:
                    if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                        hank(globais.nomeJogador, globais.pts)
                        globais.parte = 'game_over'
                        return True
                qtde_vidas[0].pop(-1)
                qtde_vidas[0].pop(-1)
                if len(objetos_segunda_parte.qtde_vidas[0]) <= 0:
                    hank(globais.nomeJogador, globais.pts)
                    globais.parte = 'game_over'
                    return True
                quadrado['x'] = 3000
                quadrado['y'] = 3000
            elif quadrado['id'] == 5 or quadrado['id'] == 6:
                if len(qtde_vidas[0]) <= 2:
                    hank(globais.nomeJogador, globais.pts)
                    globais.parte = 'game_over'
                else:
                    qtde_vidas[0].pop(-1)
                    qtde_vidas[0].pop(-1)
        elif globais.parte == 3:
            quadrado['n_colisoes'] += 1
            globais.n_colisoes_3 += 1
            if quadrado['n_colisoes'] > 40 and quadrado['id'] == 100:
                quadrado['visivel'] = False
                quadrado['n_colisoes'] = 0
                globais.pts += 20
            elif quadrado['n_colisoes'] > 10 and quadrado['id'] == 120:
                quadrado['visivel'] = False
                quadrado['n_colisoes'] = -70
                globais.pts += 40
            elif quadrado['n_colisoes'] > 10 and quadrado['id'] == 130:
                quadrado['visivel'] = False
                quadrado['n_colisoes'] = -70
                globais.pts += 60
        return True
