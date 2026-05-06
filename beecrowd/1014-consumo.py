'''
Problema: BeeCrowd: 1014
Data: 2026.05.06
Estudante: Lorenzo Waselik
'''
# Objetivo: Calcular o consumo de um automóvel em km/l

# --- ANÁLISE (LIAC) ---
# Entrada: distância total (inteiro, em km) e combústivel gasto (float, em litros)
# Processamento: consumo = X (distância) / Y (gasto de combústivel)
# Saída: consumo com 3 casas decimais seguido de "km/l"

X = int(input())
Y = float(input())

consumo = X / Y

print(f"{consumo:.3f} km/l")