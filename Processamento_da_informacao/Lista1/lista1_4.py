'''
Faca um programa contendo instrucoes para ler do teclado um n ́umero inteiro que representa uma quantidade x de
segundos. O programa deve imprimir na tela o n ́umero de horas, minutos e segundos contidos em x no formato HH:MM:SS.
Por exemplo, se x = 5000, entao o resultado dever ́a ser 01:23:20, uma vez que 5000 segundos correspondem a 1 hora, 23
minutos e 20 segundos. Se x = 3600, o resultado dever ́a ser 01:00:00 (exatamente uma hora). Um exemplo  ́e mostrado a
seguir.
Entrada lida com o comando input:
3600
Sa ́ıda correspondente a entrada:
01:00:00
'''

x = int(input())
h = x//3600
m = (x % 3600)//60
s = (x % 3600) % 60
print(f'{h:02d}:{m:02d}:{s:02d}')
