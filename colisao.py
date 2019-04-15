#from txt import pts

def collision(anzol, quadrado):
    anz3 = anzol['x'] - anzol['largura'] / 2, anzol['y'] - anzol['altura'] / 2
    anz4 = anzol['x'] + anzol['largura'] / 2, anzol['y'] - anzol['altura'] / 2
    anz1 = anzol['x'] + anzol['largura'] / 2, anzol['y'] + anzol['altura'] / 2
    anz2 = anzol['x'] - anzol['largura'] / 2, anzol['y'] + anzol['altura'] / 2

    quadV3 = quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2
    quadV4 = quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] - quadrado['altura'] / 2
    quadV1 = quadrado['x'] + quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2
    quadV2 = quadrado['x'] - quadrado['largura'] / 2, quadrado['y'] + quadrado['altura'] / 2

