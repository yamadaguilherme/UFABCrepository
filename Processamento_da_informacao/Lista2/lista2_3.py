'''
A distancia Chebyshev entre dois pontos p1 e p2 no plano cartesiano e dado por
max{| x2 − x1 |, | y2 − y1 |}.
Suponha que e dado um ponto p1=(−7, 1). Agora faca um programa que:
• Leia a partir do teclado os valores das coordenadas de um outro ponto p2 e passe-os para uma funcao, que chamaremos
de calcula distancia Chebyshev, a qual devera calcular e retornar (via comando return) a distancia Chebyshev
entre p1 e p2, de acordo com a formula descrita acima.
• Imprima o valor da distancia calculada. Importante: a(s) instrucao(coes) para impressao deve(m) estar fora da funcao
calcula distancia Chebyshev.
Atencao: o uso de funcoes e obrigatorio, a sua nao utilizacao implica em anulacao da questao.
Obs.: imprima a saıda com duas casas decimais.
'''

def entrada():
    global p1x, p1y, p2x, p2y
    p1x = -7
    p1y = 1
    p2x = int(input())
    p2y = int(input())
    
def calculadistanciaChebyshev():
    calculo = abs(p2x - p1x), abs(p2y - p1y)
    maior = max(calculo)
    distanc = "%.2f" % maior
    return distanc

def saida(x):
    print("distancia Chebyshev = ", x)
    
entrada()
calculadistanciaChebyshev()
saida(calculadistanciaChebyshev())
