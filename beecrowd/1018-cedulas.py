'''
Problema: BeeCrowd: 1018
Data: 2026.05.14
Estudante: Lorenzo Waselik
'''
# Objetivo: Com base em um valor inteiro dizer o menor número possível de cédulas de cada valor

# --- ANÁLISE (LIAC) ---
# Entrada: Um valor inteiro (int)
# Processamento: Calcular usando a divisão inteira (//) e o módulo (%)
# Saída: imprimir o valor digitado e o número de cédulas necessário começando no 100 e terminando no 1

c = int(input())

v = c

c100 = v // 100; v = v % 100
c50 = v // 50; v = v % 50
c20 = v // 20; v = v % 20
c10 = v // 10; v = v % 10
c5 = v // 5; v = v % 5
c2 = v // 2; v = v % 2
c1 = v

print(f'{c}')
print(f'{c100} nota(s) de R$ 100,00')
print(f'{c50} nota(s) de R$ 50,00')
print(f'{c20} nota(s) de R$ 20,00')
print(f'{c10} nota(s) de R$ 10,00')
print(f'{c5} nota(s) de R$ 5,00')
print(f'{c2} nota(s) de R$ 2,00')
print(f'{c1} nota(s) de R$ 1,00')