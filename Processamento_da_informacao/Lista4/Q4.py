'''
Faca um programa que:
1) Recebe 10 numeros inteiros usando input (um de cada vez).
2) Diz quantos numeros sao positivos, negativos e quantos sao iguais a zero. Imprima a quantidade de numeros positivos
em uma linha, a de numeros negativos na seguinte e a de zeros na seguinte.

'''

def entrada():
    global pos, neg, zero
    pos = 0
    neg = 0 
    zero = 0

def process():
    global pos, neg, zero
    for i in range(10):
        n = int(input())
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1
    
def saida():
    print("Quantidade de número positivo:", pos)
    print("Quantidade de número negativo:", neg)
    print("Quantidade de número zero:", zero)
    
entrada()
process()
saida()