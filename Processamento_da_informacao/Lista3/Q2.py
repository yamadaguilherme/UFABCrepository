'''
Um governo precisa de um programa Python que o ajude a operar um plano de distribuicao de beneficios sociais. Umas
das tarefas prevista nesse plano e classificar as pessoas segundo grupos prioritarios definidos por faixa etaria. Faca um
programa que leia (via o comando input) um numero inteiro que representara a idade de uma pessoa. Em seguida o seu
programa devera imprimir o mes a partir do qual o beneficio estara disponivel para essa pessoa, considerando a seguinte
tabela:
Idade (em anos) Mes
Maior que 81 Fevereiro
Maior que 71 Marco
Maior que 61 Abril
Maior que 51 Maio
Maior que 41 Junho
Maior que 31 Julho
Maior que 21 Agosto
Maior que 11 Setembro
Demais Outubro
'''

def entrada():
    global yo
    yo = int(input())

def process(x):
    if x >81:
        return "Fevereiro"
    elif x >71:
        return "Marco"
    elif x >61:
        return "Abril"
    elif x >51:
        return "Maio"
    elif x >41:
        return "Junho"
    elif x >31:
        return "Julho"
    elif x >21:
        return "Agosto"
    elif x >11:
        return "Setembro"
    else:
        return "Outubro"
def saida():
    print(process(yo))
    
entrada()
saida()
        