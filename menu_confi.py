#Este arquivo cria um menu pequeno de confirmação

import desenheiro
import globais

#Definindo um quadrado para o submenu
def desenha_menu_c():
    mc = globais.quadrado.copy()
    mc['largura'] = 50/4
    mc['altura'] = 25
    mc['cor'] = (1, 1, 0)
    desenheiro.desenha_quadrado(mc)