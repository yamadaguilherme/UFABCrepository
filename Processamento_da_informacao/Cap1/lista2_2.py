def entrada():
    global valor1, valor2
    valor1 = float(input())
    valor2 = float(input())

def calculaComissao():
    global valorfinal
    valor2pos = valor2 * 0.24
    calculo = valor2pos + valor1
    valorfinal = "%.2f" % calculo
    
def saida():
    print("Eileen Greenawalt deve receber R$", valorfinal ,"no final do mês")

entrada()
calculaComissao()
saida()