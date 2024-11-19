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