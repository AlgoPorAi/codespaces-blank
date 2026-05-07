'''
Problema: BeeCrowd: 1035
Data: 2026.05.07
Estudante: lorenzo Waselik
'''
# Objetivo: Selecionar números com base em alguns critérios

# --- ANÁLISE (LIAC) ---
# Entrada: Quatro inteiros (A,B,C e D)
# Processamento: selecionar os números usando > and e operações matemáticas
# Saída: mostrar "Valores aceitos" ou "Valores não aceitos"

A, B, C, D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (B > C) and (D > A) and (C + D > A + B) and (C > 0 and D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")