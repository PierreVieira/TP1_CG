import desenheiro
import globais
mp = globais.quadrado.copy()
mp['largura'] = 50
mp['altura'] = 100
mp['cor'] = (1,0,0)
def menu_p():
    desenheiro.desenha_quadrado(mp)