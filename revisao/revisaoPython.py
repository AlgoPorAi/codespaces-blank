# 1. Variáveis e tipos de dados: Guarda um dado para utiliza-lo durante a execução do código

Nome = "José" # Variável tipo string (str)
Idade = 53 # Variável tipo inteiro (int)
Altura = 1.55 # Variável tipo ponto flutuante (float)
MaiorDeIdade = True  # Variável tipo booleana (bool)

# 2. Operadores: São fatores que realizam operações sobre valores e variáveis

Soma = 6 + 7
Subtracao = 7 - 6
Multiplicacao = 4 * 2
Divisao = 4 / 2
DivisaoInteira = 10 // 3
Resto = 10 % 3
Potencia = 4 ** 2

# 3. Entrada de dados: Quando a pessoa se comunica com o computador

Numero = int(input("Digite um número: ")) # int representa o tipo de entrada (inteira), enquanto o input é o espaço para a digitação

# 4. Saída de dados: Quando o computador se comunica com a pessoa

print('Eu gosto de batata') # "Eu gosto de batata" será a mensagem mostrada na tela

# 5. Estruturas de repetição: são códigos que permitem que um código seja executado várias vezes

# Este código faz com que enquanto o número seja menor que 11, o programa mostre o número e some 1 a ele
while Numero < 11:
    print(f"{Numero}")
    Numero = Numero + 1

# 6. Estrutura de condição: Coloca uma condição a um código, como por exemplo, se o número for maior que 10 fazer uma coisa, senão, fazer outra

if Idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")