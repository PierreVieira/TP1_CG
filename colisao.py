#from txt import pts

def collision(anzol, quadrado):
    distancia_entre_centros = ((anzol['x'] - quadrado['x'])**2 + (anzol['y'] - quadrado['y'])**2)**0.5
    area_disponivel1 = (distancia_entre_centros*0.75)**2
    if(area_disponivel1 < anzol['area']):
        anzol['n_colisoes'] += 1
        print('Colisoes = {}'.format(anzol['n_colisoes']))
