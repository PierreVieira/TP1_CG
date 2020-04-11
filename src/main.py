from src.basico import main_basico
from src import globais

print('\033[1;31;0m====== SEJA BEM VINDO AO GAME LOLI FISHING ======\n\033[m')
globais.nomeJogador = input('\033[1;33;0mDigite o seu nome: \033[m').split()[0]
print(f'\033[4;34;0m\nBoa sorte {globais.nomeJogador}, caso atinja uma boa pontuação seu nome estará no ranking\033[m')
print('\033[1;30;0m\n================== BOM JOGO ==================\033[m')
main_basico()
