#from txt import pts
import globais
from desenheiro import deslocar_camburao
from objetos_primeira_parte import *
def collision(anzol, quadrado):
    anzV3 = anzol['x'] - anzol['largura'] / 2, anzol['y'] - anzol['altura'] / 2
    anzV4 = anzol['x'] + anzol['largura'] / 2, anzol['y'] - anzol['altura'] / 2
    anzV1 = anzol['x'] + anzol['largura'] / 2, anzol['y'] + anzol['altura'] / 2
    anzV2 = anzol['x'] - anzol['largura'] / 2, anzol['y'] + anzol['altura'] / 2

    quadV3 = quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2
    quadV4 = quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2
    quadV1 = quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2
    quadV2 = quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2

    if quadV2[0] < anzV3[0] < quadV1[0] and quadV4[1] < anzV3[1] < quadV1[1] or \
        quadV2[0] < anzV2[0] < quadV1[0] and quadV4[1] < anzV2[1] < quadV1[1] or \
        quadV2[0] < anzV1[0] < quadV1[0] and quadV4[1] < anzV1[1] < quadV1[1] or \
        quadV2[0] < anzV4[0] < quadV1[0] and quadV4[1] < anzV4[1] < quadV1[1]:
            quadrado['visivel'] = False
            anzol['n_colisoes'] += 1
            print(f'{anzol["n_colisoes"]}')
            if globais.parte == 1:
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
            elif globais.parte == 2:
                print()
