'''
Problema: beecrowd: 1008
Data: 2026.04.16
Estudante: Lorenzo Waselik
'''
# Objetivo: Mostrar o número do funcionário e seu salário com base no valor por hora e horas trabalhadas

# --- ANÁLISE (LIAC) ---
# Entrada: N (Número do funcionário) H (Horas trabalhadas) V (Valor ganho por hora)
# Processamento: Multiplicar as horas trabalhadas pelo valor ganho por hora para obter o salário
'''
Saída: exibir exatamente como:
"NUMBER: número
SALARY: U$ salário"
'''

N = int(input())
H = int(input())
V = float(input())

SAL = H * V

print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")