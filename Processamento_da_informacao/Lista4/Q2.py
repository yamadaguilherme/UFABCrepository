'''
Escreva um programa que le do teclado (com comando input):
• um numero inteiro, representando a populacao de uma cidade (vamos denotar este numero por P);
• um numero real (float), maior que 1, representando a taxa de contagio por gripe nessa cidade (vamos denotar este
numero por T xContagio). Assuma que o usuario sempre digitara um valor maior que 1 para a T xContagio, isto e,
nao precisa verificar.
Agora vamos denotar o numero de pessoas contaminadas num dia i por Cti
. Considere ainda que no dia de hoje, o dia
0 de estudo, ou seja, i = 0, essa cidade tem exatos Ct0 = 1718 contaminados. Considere tambem:
i) Somente pessoas que foram infectadas no dia i-1 podem infectar pessoas no dia i (ou seja, Cti = Cti-1 * T xContagio),
para 0 < i ≤ NumDiasImunidade, onde NumDiasImunidade e o numero de dias para conseguir a imunidade
coletiva.
ii) Qualquer pessoa ja contaminada vai sobreviver e ter imunidade pelo resto do tempo dentro do modelo.
iii O calculo do numero de pessoas imunizadas na cidade e cumulativo, por exemplo, o numero de pessoas imunizadas no
dia numero 5 e igual a Ct0 + Ct1 + Ct2 + Ct3 + Ct4 + Ct5.
iv) A imunidade coletiva nessa populacao ocorrera quando o numero de contaminados for maior ou igual a 72.0% da
populacao. Em outras palavras, as contaminacoes continuam ocorrendo enquanto o numero de pessoas imunizadas
for menor do que 0.72 * P.
Dadas a populacao da cidade e a taxa de contagio (lidas via comando input), o seu programa deve imprimir em quantos
dias a cidade atingira a imunidade coletiva. Abaixo um exemplo com os formatos de entrada e saida

'''
def entrada():
    global P, TxC, Ct, Cti, NumD
    P = int(input())
    TxC = float(input())
    Ct = 1718
    Cti, NumD = 0, 0
    
def process():
    global Cti, NumD, Ct
    while Cti < 0.72*P:
        Ct = Ct * TxC
        Cti += Ct
        NumD += 1

def saida():
    print(f"A cidade conseguiu imunidade coletiva em {NumD} dias")

entrada()
process()
saida()