'''
A formula abaixo representa um polinomio definido por partes. Esse tipo de funcao e bastante utilizado em interpolacao
numerica e computacao grafica:
f (x) = (x - 2)2 + 1, se 0 ≤ x < 3
f (x) = 1 - (x - 4)2- 2, se 3 ≤ x ≤ 8
f (x) = 0, se x < 0 ou x > 8

Escreva um programa que recebe do usuario um numero inteiro x e apresente o valor de f(x).
'''

def entrada():
    global x
    x = int(input())
    
def fx():
    global fx
    if 0 <= x <3:
        fx = (x-2)**2 + 1
    elif 3 <= x <= 8:
        fx = 1 - ((x-4)**2) - 2
    else:
        fx = 0

def saida():
    print(f"f({x}) = {fx}")

entrada()
fx()
saida()