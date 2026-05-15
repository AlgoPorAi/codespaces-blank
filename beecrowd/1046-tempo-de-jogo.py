'''
Problema: BeeCrowd: 1046
Data: 2026.05.14
Estudante: Lorenzo Waselik
'''
# Objetivo: Baseado em duas horas diferentes dizer quanto em tempo durou um jogo

# --- ANÁLISE (LIAC) ---
# Entrada: Dois valores inteiros na mesma linha (hora inicial e final)
# Processamento: converter o início e o fim para o total
#                se o fim for menor ou igual ao início, o jogo "virou a meia-noite"
# Saída: "O JOGO DUROU H HORA(S)"

hi, hf = map(int, input().split())

if hi > hf:
    ttm = (hf - hi) + 24
else:
    ttm = hf - hi

if ttm == 0:
    ttm = 24

print(f"O JOGO DUROU {ttm} HORA(S)")