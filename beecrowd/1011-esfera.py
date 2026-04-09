'''
Problema: beecrowd: 1011
Data: 2026.4.9
Estudante: Lorenzo Waselik
'''
# Objetivo: Ler o raio de uma esfera e calcular seu volume com a fórmula (4/3) * pi * R³

# --- ANÁLISE (LIAC) ---
# Entrada: Um número de ponto flutuante (o raio R)
# Processamento: Aplicar a fómula do volume da esfera
# Saída: Exibir no formato "VOLUME = valor" com 3 casa decimais

# Float() - converte o valor lido para número decimal (ponto flutuante)
R = float(input())

# O enunciado pede para atribuir pi como constante - não usar math.pi
pi = 3.14159

# 4.0/3 garante divisão decimal (não imteira) - conforme dica do enunciado
# R**3 - R elevado à terceira poência (R³)
V = (4.0 / 3) * pi * R ** 3

# :.3f - formta o número com exatamente 3 casas decimais
print(f"VOLUME = {V:.3f}")