# ==================================
# Arquivo:      telas.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Lorenzo Waselik
# Data:         2026.08.04
# Conceitos: 
# ==================================

# Definicao da moldura (Caracteres e Tamanho)
CAR = "="
TAM = 40

# Funcao para desenhar uma linha na tela
def linha():
    print(CAR * TAM)

# Funcao para desenhar um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()

