# MATEMATICA

Jogo autoral do meu fliperama. Abre pela opcao [4] do menu.
Autor: Lorenzo Waselik

## A regra

[Tres ou quatro linhas: o que o jogador faz, o que o programa faz em resposta e quando o jogo termina.]

## Como jogar

1. Dentro da pasta `fliperama`, rode `python3 main.py`.
2. Escolha a opcao `[4]` no menu.
3. selecione a dificuldade e o computador cria uma conta selecionando dois numeros aleatorios e a operacao (facil: soma ou subtracao (pode escolher), medio: multiplicacao e dificil: potenciacao), o computador mostra a conta, e voce resolve e digita o resultado.

## O que eu reusei do projeto, e onde

| Peca | De qual modulo | Onde eu uso | Para que serve ali |
|---|---|---|---|
| `titulo()` | `telas.py` | `meujogo.py`, linha 18 | desenha a testeira do jogo |
| `linha()` | `telas.py` | `meujogo.py`, linha 19 | fecha a tela no fim da partida |
| `ler_numero()` | `modulos.py` | `meujogo.py`, nao foi usado | pede o numero e recusa fora do intervalo |
| contagem da partida | `placar.py` | `main.py`, linha [N] | soma 1 em `vezes_jogado` a cada partida |

[Se voce tambem usou a `buscar` do `jogadores.py` para perguntar quem
vai jogar, acrescente uma linha aqui dizendo onde.]

## Exemplo de execucao

```
========================================
               MATEMATICA               
========================================
========================================
Escolha uma dificuldade:
[0] - Facil
[1] - Media
[2] - Dificil
========================================
Dificuldade escolida: 
```

## O que ainda nao funciona

- optei por nao colocar divisao e modulo pois a maioria daria numeros decimais e nao consegui achar um codigo para isso.
