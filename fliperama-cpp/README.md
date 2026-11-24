# Fliperama em C++ (MeuApp v4.0)

## O que e
O fliperama e um projeto que tem o cadastro e a busca de jogadores alem do adivinhe o numero entre outros. Ele surgiu no segundo trimestre na linguagem python em que o adptamos em cada linguagem nova que aprendemos.

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: O arquivo principal do jogo, ele guarda os codigos tanto dos jogos quanto da funcao cadastrar.
- jogadores.csv: um arquivo que guarda os jogadores, em cada linha a "nome do jogador,partidas jogadas".

## C x C++: o que mudou

| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 69) | apelidos.push_back(novo) (l. 91) |
| comparar apelidos | strcmp(...) == 0 (l. 51) | == (l. 56) |
| a funcao que cadastra | int cadastrar(..., int qtd) (l. 58) | void cadastrar(... &apelidos, ...) (l. 85) |

## O que o C++ decidiu por mim
Em C, eu precisava definir o tamanho maximo para um vetor, o que em C++ nao acontece, pois a cada push__back o vetor cresce sozinho, sem precisar de alteracao manual.

## Autoavaliacao

| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | C | fliperama.cpp linha 1 a 6, .gitignore linha 1 a 6 |
| 2. Cadastro: vectors e referencia | C | fliperama.cpp linha 85 a 94 |
| 3. Jogo e partidas | C | fliperama.cpp linha 108 a 137 |
| 4. Persistencia | C | fliperama.cpp linha 63 a 83 |
| 5. Documentacao e comparacao | C | README.md linha 1 a 33 |