'''
Faca um programa que:
• leia o salario fixo e o valor das vendas efetuadas no mes (em Reais) pelo vendedor Eileen Greenawalt;
• calcule e imprima o valor total (em Reais) que o Eileen Greenawalt recebera no fim do mes, considerando que ele
ganha 24% de comissao sobre o valor das vendas por ele efetuadas.
Fazer um modulo (funcao) chamado calculaComissao que recebe como parametros um valor (em vendas efetuadas) e
uma porcentagem. Essa funcao deve retornar quanto o vendedor ganhara de comissao, considerando esse valor em vendas
efetuadas e uma porcentagem (no caso, 24%).
Atencao: o uso de funcoes e obrigatorio, a sua nao utilizacao implica em anulacao da questao.
Obs.: imprima a saıda com duas casas decimais.
'''

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
