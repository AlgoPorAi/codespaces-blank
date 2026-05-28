
# Disciplina: Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto   : Jogo "Adivinhe o Número"
# Arquivo:  : adivinhe.py
# Autor     : Lorenzo Waselik
# Data      : 2026.05.28

import random

# 1) Sorteamos o número secreto entre 1 e 10
numero_secreto = random.randint(1, 10)

# 2) Pedimos um palpite (input devolve TEXTO; convertemos para inteiro)
palpite = int(input("Digite um número de 1 a 10: "))

# 3) Comparamos o palpite com o número secreto
if palpite == numero_secreto:
    print("Acertou! O número era", numero_secreto)
elif palpite < numero_secreto:
    print("Muito baixo! Tente um número maior.")
else:
    print("Muito alto! Tente um número menor.")