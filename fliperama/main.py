# ==================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Lorenzo Waselik
# Data:         2026.08.04
# Conceitos: 
# ==================================

# Importar funcoes de arquivos (modulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao
from ppt import jogar_ppt
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
from parimpar import jogar_parimpar
from matematica import jogar_matematica
NOMES_DOS_JOGOS = ["Adivinhe o Numero", "Pedra-Papel-Tesoura", "Par ou Impar"]
vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

NOME_DO_DONO = "LORENZO"
OPCOES = ["0", "1", "2", "3", "4", "5"]

def mostrar_placar():
    titulo("PLACAR")
    for i in range(len(vezes_jogado)):
        print(NOMES_DOS_JOGOS[i] + ": " + str(vezes_jogado[i]) + "x")

while True:
    titulo("FLIPERAMA DO " + NOME_DO_DONO)
    print("[1] Adivinhe o Numero")
    print("[2] Pedra-Papel-Tesoura")
    print('[3] Par ou Impar')
    print('[4] Matematica')
    print('[5] Jogadores')
    print("[0] Sair")
    linha()
    opcao = ler_opcao("Escolha uma opcao", OPCOES)

    if opcao == "0":
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo("Ate a proxima!")
        break

    if opcao == '5':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
        vezes_jogado[indice] = vezes_jogado[indice] + 1

    if opcao == "1":
        jogar_adivinhe()
    elif opcao == "2":
        jogar_ppt()
    elif opcao == "3":
        jogar_parimpar()
    elif opcao == '4':
        jogar_matematica()

    input('Pressione Enter para voltar ao menu... ')