'''
Problema: BeeCrowd: 1044
Data: 2026.05.06
Estudante: Lorenzo Waselik
'''
# Objetivo: Verificar se dois inteiros são múltiplos entre si

# --- ANÁLISE (LIAC) ---
# Entrada: D ois inteiros A e B na mesma linha separados por espaço
# Processamento: Identificar maior e menor, verificar se maior % menor == 0
# Saída: "Sao multiplos" ou "Não sao multiplos"

A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")