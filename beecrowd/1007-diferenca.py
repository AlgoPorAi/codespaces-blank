'''
Problema: BeeCrowd: 1007
Data: 2026.05.06
Estudante: Lorenzo waselik
'''
# Objetivo: Ler quatro inteiros e calcular DIFERENCA = (A * B) - (C * D)

# --- ANÁLISE (LIAC) ---
# Entrada: quatro valores inteiros A, B, C e D (um por linha)
# Processamento: diferença entre o produto A*B e o produto C*D
# Saída: "DIFERENCA = valor" (inteiro, letras maiúsculas, espaços ao redor do =)

A = int(input())
B = int(input())
C = int(input())
D = int(input())

dif = (A * B) - (C * D)

print(f"DIFERENCA = {dif}")