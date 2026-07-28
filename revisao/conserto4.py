jogada = input("pedra, papel ou tesoura? ")
jogada_final = jogada.lower().strip()
if jogada_final == "pedra" or jogada_final == "papel" or jogada_final == "tesoura":
    print("Jogada valida:", jogada)
else:
    print("Jogada Inválida!")

# O código não funcionou com "Pedra" pois o código não deixava as letras minúsculas, assim considerando Pedra e pedra duas coisas diferentes
