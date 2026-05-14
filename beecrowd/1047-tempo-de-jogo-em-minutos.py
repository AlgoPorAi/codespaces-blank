'''
Problema: BeeCrowd: 1047
Data: 2026.05.14
Estudante: Lorenzo Waselik
'''
# Objetivo: Calcular a DURAÇÃO de um jogo (em horas e minutos), sabendo
#           a hora de início (hi:mi) e a hora de fim (hf:mf)
#           O jogo dura no MÍNIMO 1 minuto e no MÁXIMO 24 horas

# --- ANÁLISE (LIAC) ---
# Entrada: 4 inteiros na mesma linha - hi mi hf mf (hora/minuto inicial e final)
# Processamento: converter início  e fim para o total em MINUTOS
#                se o fim for menor ou igual ao início, o jogo "virou a meia noite"
#Saída: "O JOGO DUROU H HORA(S) E M MINUTO(S)"

hi, mi, hf, mf = map(int, input().split())

tim = (hi * 60) + mi
tfm = (hf * 60) + mf

if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim

if ttm == 0:
    ttm = 24 * 60

print(f"O JOGO DUROU {ttm // 60} HORA(S) E {ttm % 60} MINUTO(S)")