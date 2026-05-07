'''
Problema: BeeCrowd: 1012
Data: 2026.05.07
Estudante: Lorenzo Waselik
'''
# Objetivo: ler três valores com ponto flutuante (A, B e C) e calcular a área de diferente figuras

# --- ANÁLISE (LIAC) ---
# Entrada: Três valores de ponto flutuante (A, B e C)
# Processamento: Realizar a respectiva conta de área de cada figura utilizando sua respectiva fórmula
# Saída: exibir como "TRIANGULO: valor..." com uma figura em cada linha

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

Tri = (A * C) / 2
Cir = 3.14159 * C ** 2 
Tra = ((A + B) * C) / 2
Qua = B ** 2
Ret = A * B

print(f"TRIANGULO: {Tri:.3f}")
print(f"CIRCULO: {Cir:.3f}")
print(f"TRAPEZIO: {Tra:.3f}")
print(f"QUADRADO: {Qua:.3f}")
print(f"RETANGULO: {Ret:.3f}")