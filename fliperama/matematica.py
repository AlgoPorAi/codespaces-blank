# ===============================================================
# ARQUIVO: matematica.py (pasta fliperama)
# Disciplina: Pensamento Computacional, Algoritmos e Programacao
#             (2026-PCAP)
# Aula: 23 - o jogo autoral do seu fliperama
# Autor: Lorenzo Waselik
# Conceitos: Reuso de modulo proprio, funcao sem retorno, entrada validada
# ===============================================================

from telas import titulo, linha
from modulos import ler_opcao
import random

def jogar_matematica():
    '''
    Gera uma conta aleatoria com o sinal escolhido para que o jogador resolva
    '''
    titulo('MATEMATICA')
    linha()

    print('Escolha uma dificuldade:')
    print('[0] - Facil')
    print('[1] - Media')
    print('[2] - Dificil')
    linha()

    dificuldade = ler_opcao('Dificuldade escolida', ['0', '1', '2'])
    linha()

    NumeroA = random.randint(0, 9)
    NumeroB = random.randint(0, 9)

    if dificuldade == '0':
        operacao = ler_opcao('Selecione a operacao: [0] - soma | [1] - subtracao: ', ["0", "1"])
        linha()

        if operacao == '0':
            conta = NumeroA + NumeroB
            print('Resolva esta conta:')
            print(f'{NumeroA} + {NumeroB}')
            linha()
            resposta = int(input('Resultado: '))
            linha()
            if resposta == conta:
                print('Parabens! Voce acertou!')
                linha()
            else:
                print('Voce errou! Melhor ir fazer algumas contas')
                linha()
        elif operacao == '1':
            conta = NumeroA - NumeroB

            print('Resolva esta conta:')
            print(f'{NumeroA} - {NumeroB}')
            linha()
            resposta = int(input('Resultado: '))
            if resposta == conta:
                print('Parabens! Voce acertou!')
                linha()
            else:
                print('Voce errou! Tente uma operacao mais facil!')
                linha()
    elif dificuldade == '1':
        conta = NumeroA * NumeroB
        print('Resolva esta conta:')
        print(f'{NumeroA} * {NumeroB}')
        linha()
        resposta = int(input('Resultado: '))
        linha()
        if resposta == conta:
            print('Parabens! Voce acertou!')
            linha()
        else:
            print('Voce errou! Tente uma operacao mais facil')
            linha()
    elif dificuldade == '2':
        conta = NumeroA ** NumeroB
        print('Resolva esta conta:')
        print(f'{NumeroA} ** {NumeroB}')
        linha()
        resposta = int(input('Resultado: '))
        linha()
        if resposta == conta:
            print('Parabens! Voce acertou!')
            linha()
        else:
            print('Voce errou! Tente uma operacao mais facil')
            linha()