'''
Problema: BeeCrowd: 1006
Data: 2026.04.23
Estudante; Lorenzo Waselik
'''
# Objetivo: Ler 3 notas com pesos diferentes e calcular a média ponderada

# --- ANÁLISE (LIAC) ---
# Entrada: 3 valores de ponto flutuante (float) A, B e C
# Processamento: média ponderada (A * 2 + B * 3 + C * 5) / 10
# Saída: mostrar como "MEDIA = valor"

A = float(input())
B = float(input())
C = float(input())

media = (A * 2 + B * 3 + C * 5) / 10

print(f"MEDIA = {media:.1f}")