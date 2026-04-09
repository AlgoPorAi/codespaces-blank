'''
Problema: beecrowd: 1002
Data: 2026.4.9
Estudante: Lorenzo Waselik
'''
# Objetivo: Calcular a área de uma circunferência com a fórmula pi*raio²=área

# --- ANÁLISE (LIAC) ---
# Entrada: Um valor decimal
# Processamento: Aplicar o valor digitado na fórmula pi*R²
# Saída: Deve ser exibido como "A = área"

R = float(input())

pi = 3.14159

AREA = pi * R ** 2

print(f"A={AREA:.4f}")