'''
Problema: BeeCrowd: 1050
Data: 2026.04.30
Estudante: Lorenzo Waselik
'''
# Objetivo: Ler um código DDD e informar a qual cidade ele pertence

# --- ANÁLISE (LIAC) ---
# Entrada: Um número inteiro representando o código DDD
# Processamento: Comparar o DDD lido com cada código da tabela usando if/elif/else
# Saída: Nome da cidade correspondente, ou "DDD não cadastrado" se não encontrado

DDD = int(input())

if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("Sao Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")