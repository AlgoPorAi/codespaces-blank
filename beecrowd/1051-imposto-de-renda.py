'''
Problema: BeeCrowd: 1051
Data: 2026.05.15
Estudante: Lorenzo Waselik
'''
# Objetivo: Calcular o imposto de renda baseado no salário

# --- ANÁLISE (LIAC) ---
# Entrada: um valor de ponto flutuante (float)
# Processamento: descontar o valor isento de impostos e multiplicar respectivos salários pelas respectivas porcentagens
# Saída: "R$ valor" ou "Isento"

salario = float(input())

if salario <= 2000.00:
    print("Isento")
elif salario <= 3000.00:
    i = (salario - 2000.00) * 0.08
    print(f"R$ {i:.2f}")
elif salario <= 4500.00:
    i = (1000.00 * 0.08) + ((salario - 3000) * 0.18)
    print(f"R$ {i:.2f}")
else:
    i = (1000.00 * 0.08) + (1500.00 * 0.18) + ((salario - 4500.00) * 0.28)
    print(f"R$ {i:.2f}")