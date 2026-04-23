'''
Problema: BeeCrowd: 1020
Data: 2026.04.23
Estudante: Lorenzo Waselik
'''
# Objetivo: Exibir a idade em anos, meses e segundos com base nos dia

# --- ANÁLISE (LIAC) ---
# Entrada: Variável N (idade em dias)
# Processamento: extrair anos,meses e dias por base na divisão inteira e módulo
'''
Saída: exibir como:
ano(s)
mes(es)
dia(s)
'''

N = int(input())

a = N // 365

N = N % 365

m = N // 30

d = N % 30

print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")