'''
Um site que vende unidades de ar-condicionado precisa de um programa para fornecer recomendacoes aos seus clientes sobre
qual a potencia (em BTUs/h) do equipamento que eles precisam comprar. A potencia do ar-condicionado recomendada
pelo programa dependera da area do comodo em metros quadrados (m^2) fornecida pelo usuario, conforme a tabela a seguir:
    Area  (m^2)         Potencia (BTU/h)
    Area < 12.1     Recomendamos 9300 BTU/h
12.1 ≤ Area <  17.1 Recomendamos 12300 BTU/h
17.1 ≤ Area <  22.1 Recomendamos 15300 BTU/h
22.1 ≤ Area <  27.1 Recomendamos 18300 BTU/h
27.1 ≤ Area  ≤ 32.1 Recomendamos 21300 BTU/h
    Area  > 32.1        Sem recomendacao
Escreva um programa que le um valor de area em metros quadrados, o qual deve ser um numero real (float). Em seguida,
seu programa deve imprimir uma recomendacao de potencia, com base na tabela acima.
'''

def entrada():
    global m    
    m = float(input())

def process(x):
    if x > 32.1:
        return ": Sem recomendacao"
    elif x >= 27.1:
        return ": Recomendamos 21300 BTU/h"
    elif x >= 22.1:
        return ": Recomendamos 18300 BTU/h"
    elif x >= 17.1:
        return ": Recomendamos 15300 BTU/h"
    elif x >= 12.1:
        return ": Recomendamos 12300 BTU/h"
    else:
        return ": Recomendamos 9300 BTU/h"
def saida():
    print("Para area =", m, process(m))
    
entrada()
saida()