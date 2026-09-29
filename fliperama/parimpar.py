import random
from modulos import ler_opcao
from telas import titulo, linha

def jogar_parimpar():
    titulo('PAR OU IMPAR')
    linha()

    pontos_jogador = 0
    pontos_maquina = 0

    rodada = 1

    while pontos_jogador < 3 and pontos_maquina < 3 and rodada < 5:
    
        print("--- Rodada", rodada, "---")   
        jogada_maquina = random.randint(0, 5)
        jogada_jogador = int(input("Sua jogada (0 a 5): "))
        aposta_bruta = ler_opcao("Sua aposta (par ou impar): ", ['par', 'impar'])
        linha()
        aposta = aposta_bruta.lower().strip()
        opcoes = ["par", "impar"]
    
        soma = jogada_jogador + jogada_maquina

        def resultado(aposta, soma):
            if soma % 2 == 0:
                paridade = "par"
            else:
                paridade = "impar"

            if paridade == aposta:
                return "jogador"
            else:
                return "maquina"

        resultado = resultado(aposta, soma)

        if aposta not in opcoes:
            print("Aposta invalida!")

        print(f"Sua aposta: {aposta}")
        print(f"Sua jogada: {jogada_jogador}")
        print(f"Sua jogada da maquina: {jogada_maquina}"),
        print(f"Soma: {soma}")
        print(f"Ganhador: {resultado}")
        linha()

        if resultado == "jogador":
            print("Parabens! Voce ganhou!")
            linha()
            pontos_jogador = pontos_jogador + 1
        else:
            print("A maquina ganhou!")
            linha()
            pontos_maquina = pontos_maquina + 1
        rodada = rodada + 1
    
    print("Placar final -> Voce:", pontos_jogador, "| Maquina:", pontos_maquina)
    linha()