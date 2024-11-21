'''
Dados tres numeros f, e e y, considere a equacao

vox = (f × e^2 × y^3)/(f + e + y)

Faca um programa que leia do teclado tres numeros reais f, e e y, e imprima o resultado da equacao, conforme descrito
acima. Implemente de tal modo que o seu codigo contenha uma funcao correspondente a esta equacao, a qual deve receber
como argumentos os valores de f, e e y, e retornar um numero real como resultado do calculo.
Atencao: o uso de funcoes e obrigatorio, a sua nao utilizacao implica em anulacao da questao.
Obs.: imprima a saıda com duas casas decimais.
'''

def entrada():
    global f, e, y 
    f = int(input())
    e = int(input())
    y = int(input())

def vox(f, e, y):
    global vox
    vox1 = (f * (e**2) * (y**3))/(f+e+y)
    vox = "%.2f" % vox1
    return vox

def saida():
    print("vox = ", vox)
    
entrada()
vox(f, e, y)
saida()
