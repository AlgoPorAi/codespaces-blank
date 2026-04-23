'''
Problema: BeeCrowd: 1019
Data: 2026.04.23
Estudante: Lorenzo Waselik
'''
# Objetivo:  Ler uma duração em segundos e convertê-la para horas:minutos:segundos

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro N representando segundos totais
# Processamento: extrair horas, minutos e segundos restantes por divisão inteira e módulo
# Saída: no formato h:m:s (sem zeros à esquerda - 0:9:16, não 00:09:16)

N = int(input())

h = N // 3600

N = N % 3600

m = N // 60

s = N % 60

print(f"{h}:{m}:{s}")