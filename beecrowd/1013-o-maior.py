'''
Problema: BeeCrowd: 1013
Data: 2026.05.07
Estudante: Lorenzo Waselik
'''
# Objetivo: Calcular o maior número entre A, B e C

# --- ANÁLISE (LIAC) ---
# Entrada: Três valores inteiros (A, B e C)
# Processamento: Utilizar a fórmula (a + b + abs(a - b)) / 2
# Saída: "resultado eh o maior"

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

maiorAB = (A + B + abs(A - B)) / 2

maiorABC = (maiorAB + C + abs(maiorAB - C)) / 2

print(f"{maiorABC:.0f} eh o maior")