'''
Faca um programa que:
1) Recebe um numero n inteiro ou real (float).
2) Se o numero for > 108, imprima Meta atingida e saia do laco. Caso contrario, imprima Insuficiente e volte ao
passo 1 (lendo um novo numero n). Voce deve ler no maximo 5 numeros.

'''
def entrada():
    global n
    n = float(input())

def process():
    global mystr, n
    for i in range(5):
        if n > 108:
            mystr = "Meta Atingida"
            continue
        else:
            n = float(input())
            print("Insuficiente")

def saida():
    print(mystr)

entrada()
process()
saida()