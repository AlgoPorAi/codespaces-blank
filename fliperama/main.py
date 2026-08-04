# ==================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Lorenzo Waselik
# Data:         2026.08.04
# Conceitos: 
# ==================================

# Importar funções de arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao

NOME_DO_DONO = "LORENZO"
OPCOES = ["0", "1"]

while True:
    titulo("FLIPERAMA DO " + NOME_DO_DONO)
    print("1 - Jogo adivinhe o número")
    print("0 - Sair do fliperama")
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        print("Até a próxima!")
        break
    elif opcao == "1":
        jogar_adivinhe()