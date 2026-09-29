# ==================================
# Arquivo:      ppt.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Lorenzo Waselik
# Data:         2026.08.11
# Conceitos: 
# ==================================

from random import randint
from telas import titulo, linha
from modulos import ler_opcao

JOGADAS = ["PEDRA", "PAPEL", "TESOURA"]

def quem_vence(jogador, computador):
    if jogador == computador:
        return "empate"
    if jogador == (computador + 1) % 3:
        return "jogador"
    return "computador"

def mostrar_jogadas():
    print("[0] Pedra")
    print("[1] Papel")
    print("[2] Tesoura")
    linha()

def jogar_ppt():
    titulo("PEDRA-PAPEL-TESOURA")

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao("Sua jogada", ["0", "1", "2"]))
        computador = randint(0, 2)

        print("Voce jogou " + JOGADAS[jogador] + ".")
        print("O PC jogou " + JOGADAS[computador] + ".")

        resultado = quem_vence(jogador, computador)

        if resultado == "empate":
            print("Empate! Ninguem pontua.")
        elif resultado == "jogador":
            pontos_jogador = pontos_jogador + 1
            print("Voce venceu a rodada.")
        else:
            pontos_computador = pontos_computador + 1
            print("O PC venceu a rodada.")

        print("Placar: voce " + str(pontos_jogador) +
        " x " + str(pontos_computador) + " PC")

    if pontos_jogador > pontos_computador:
        titulo("VOCE VENCEU A PARTIDA!")
    else:
        titulo("O PC VENCEU A PARTIDA!")