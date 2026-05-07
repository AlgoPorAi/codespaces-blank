'''
Problema: BeeCrowd: 1010
Data: 2026.05.07
Estudante: Lorenzo Waselik
'''
# Objetivo: Ler código, quantidade e valor unitário de duas peças e calcular o total a pagar

# ---- ANÁLISE (LIAC) ---
# Entrada: duas linhas; cada uma com código (int), quantidade (int) e valor unitário (float)
# Processamento: Total = (qtd1 * val1) + (qtd2 * val2)
# Saída: "VALOR A PAGAR: R$ total" com duas casas decimais

cod1, qtd1, val1 = input().split()

qtd1 = int(qtd1)
val1 = float(val1)

cod2, qtd2, val2 = input().split()

qtd2 = int(qtd2)
val2 = float(val2)

total = (qtd1 * val1) + (qtd2 * val2)

print(f"VALOR A PAGAR: R$ {total:.2f}")