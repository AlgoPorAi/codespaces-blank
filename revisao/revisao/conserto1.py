print("=== ADIVINHE O NUMERO ===")

segredo = 7
palpite = int(input("Digite um numero de 1 a 10: "))
if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era", segredo)

# O código original não funcionava pois o input não continha o int, fazendo o código assim interpretar o 7 digitado pelo jogador como string
