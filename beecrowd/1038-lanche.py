'''
Problema: BeeCrowd: 1038
Data: 2026.05.14
Estudante: Lorenzo Waselik
'''
# Objetivo: Calcular o valor da conta com base no produto escolhido e sua quantidade

# --- ANÁLISE (LIAC) ---
# Entrada: Um valor para o número do lanche e um para a quantidade
# Processamento: Multiplicar o valor do lanche pela quantidade
# Saída: "Total: R$ valor"

V, Q = input().split()

V = int(V)
Q = int(Q)

if V == 1:
    valor = 4.00
elif V == 2:
    valor = 4.50
elif V == 3:
    valor = 5.00
elif V == 4:
    valor = 2.00
elif V == 5:
    valor = 1.50

total = valor * Q

print(f"Total: R$ {total:.2f}")