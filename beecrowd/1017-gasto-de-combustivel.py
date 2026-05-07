'''
Problema: BeeCrowd: 1017
Data: 2026.05.07
estudante: Lorenzo Waselik
'''
# Objetivo: Calcular os litros necessários para uma viagem usando horas de viagem e velocidade média

# --- ANÁLISE (LIAC) ---
# Entrada: Horas de viagem (int) e Velocidade média (int)
# Processamento: multiplicar tempo por velocidade e depois dividir prlo km/litros
# Saída: Litros necessários com três digitos depois da virgula

KL = 12
HV = int(input())
VM = int(input())

KM = HV * VM

LN = KM / KL

print(f"{LN:.3f}")     