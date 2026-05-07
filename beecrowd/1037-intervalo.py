'''
Problema: BeeCrowd: 1037
Data: 2026.05.07
Estudante: Lorenzo Waselik
'''
# Objetivo: Ler um valor float e indicar em qual intervalo ele se encontra

# --- ANÁLISE (LIAC) ---
# Entrada: Um número de ponto flutuante qualquer
'''
Processamento: Verificar em qual dos intervalos o valor se enquadra
[o,25] - 0 <= valor <= 25
[25,50] - 25 < valor <= 50
[50,75] - 50 < valor <= 75
[75,100] - 75 < valor <= 100
fora - qualquer outro valor
'''
# Saída: mensagem com o intervalo correspondente ou "Fora de intervalo"

V = float(input())

if 0 <= V <= 25:
    print("Intervalo [0,25]")
elif 25 < V <= 50:
    print("Intervalo (25,50]")
elif 50 < V <= 75:
    print("Intervalo (50,75]")
elif 75 < V <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")