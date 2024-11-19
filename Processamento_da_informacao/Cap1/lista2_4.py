'''
No Brasil a moeda e o Real (R$) e a Casa da Moeda atualmente imprime cedulas nos valores R$ 2, R$ 5, R$ 10, R$ 20,
R$ 50, R$ 100 e R$ 200. Suponha que em um paıs peculiar, a moeda corrente e a JabuticabaCoins (OZ$), e que a Casa
da Moeda desse paıs imprime cedulas dessa moeda nos seguinte valores: 1, 7, 8, 13, 33.
Faca um programa que leia um numero inteiro e calcule o menor numero de cedulas de JabuticabaCoins no qual o
valor lido pode ser decomposto. Em outras palavras, dado um valor em JabuticabaCoins (numero inteiro, lido teclado),
seu programa deve imprimir – para cada valor de cedula existente – a quantidade mınima de cedulas necessarias para formar
esse valor lido do teclado. Veja um exemplo de entrada e saıda abaixo.
Fazer um modulo (funcao) chamado calculaDinheiro que recebe como parametros um valor inteiro qualquer e o valor
de cada um dos tipos de cedula (1, 7, 8, 13, 33). Essa funcao deve retornar – para cada valor de cedula existente – a
quantidade mınima de cedulas de JabuticabaCoins necessaria para formar esse valor.
Atencao: o uso de funcoes e obrigatorio, a sua nao utilizacao implica em anulacao da questao.

'''
def entrada():
    global total
    total = int(input())

def process():
    global oz33, oz13, oz8, oz7, oz1
    oz33 = total//33
    oz13 = (total%33)//13
    oz8 = ((total%33)%13)//8
    oz7 = (((total%33)%13)%8)//7
    oz1 = ((((total%33)%13)%8)%7)//1

def saida():
    print(oz33, "JabuticabaCoin(s) de OZ$ 33")
    print(oz13, "JabuticabaCoin(s) de OZ$ 13")
    print(oz8, "JabuticabaCoin(s) de OZ$ 8")
    print(oz7, "JabuticabaCoin(s) de OZ$ 7")
    print(oz1, "JabuticabaCoin(s) de OZ$ 1")

entrada()
process()
saida()
