# Disciplina: Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto: Jogo "Par ou Ímpar"
# Arquivo: par_impar.py
# Autor: Lorenzo Waselik
# Data: 2026.06.25

import random

pontos_jogador = 0
pontos_maquina = 0

rodada = 1

while pontos_jogador < 3 and pontos_maquina < 3 and rodada < 5:
    
    print("--- Rodada", rodada, "---")   
    jogada_maquina = random.randint(0, 5)
    jogada_jogador = int(input("Sua jogada (0 a 5): "))
    aposta_bruta = input("Sua aposta (par ou ímpar): ")
    aposta = aposta_bruta.lower().strip()
    opcoes = ["par", "impar"]
    
    soma = jogada_jogador + jogada_maquina

    def resultado(aposta, soma):
        if soma % 2 == 0:
            paridade = "par"
        else:
            paridade = "impar"

        if paridade == aposta:
            return "jogador"
        else:
            return "maquina"

    resultado = resultado(aposta, soma)

    if aposta not in opcoes:
        print("❌ Aposta inválida!")

    print(f"Sua aposta: {aposta}")
    print(f"Sua jogada: {jogada_jogador}")
    print(f"Sua jogada da máquina: {jogada_maquina}"),
    print(f"Soma: {soma}")
    print(f"Ganhador: {resultado}")

    if resultado == "jogador":
        print("🎉 Parabéns! Você ganhou!")
        pontos_jogador = pontos_jogador + 1
    else:
        print("💀 A máquina ganhou!")
        pontos_maquina = pontos_maquina + 1
    rodada = rodada + 1
    
print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)
