# Fliperama em C (MeuApp v3.0)

## O que e

O programa do fliperama tem um jogo (adivinhe o numero), um locar para cadastrar apelidos, um para listar os apelidos e outro para sair, este programa e uma adaptacao do fliperama feito em python no segundo trimestre na disciplina PCAP com o prof Berssa.

## Como compilar e rodar

gcc -Wall fliperama.c -o fliperama
./fliperama

## Arquivos

- fliperama.c: o codigo principal, tem o jogo e os codigos para digitar e alvar os apelidos.
- jogadores.csv: cada linha guarda um apelido e quantas partidas foram jogadas por essa pessoa

## Python x C: o que mudou

| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
| guarda um jogador | jogadores.append(novo) (linha 42) | strcpy(apelidos[qtd], novo) (linha 69) |
| compara apelidos | == (linha 50) | strcmp(...) == 0 (linha 51) |
| abrir sem arquivo | exists(ARQUIVO) (linha 127) | fopen == NULL (linha 129) |

## O que o C me obrigou a decidir

Em Python as linhas quebravam sozinhas, enquanto no C apos cada printf temos que utilizar "\n"

## Autoavaliacao

| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | B | fliperama.c linha 1 a 6 |
| 2. Cadastro: menu, funcoes e vetores | C | fliperama.c linha 142 |
| 3. Jogo e partidas | B | fliperama.c linhas 87 e 118 |
| 4. Persistencia | C | jogadores.csv linha 1 a 3 |
| 5. Documentacao e comparacao | C | README.md linhas 19 a 23 |