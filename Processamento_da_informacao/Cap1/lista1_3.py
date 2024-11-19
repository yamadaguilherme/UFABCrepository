'''
Escreva um programa que ajude uma loja a fazer uma venda cujo pagamento  ́e parcelado. Assuma que a loja divide o
preco em 21 parcelas iguais e sem quaisquer acrescimos (juros, multas, etc). Faca programa que:
• leia do teclado o preco do produto;
• imprima quanto custar ́a cada parcela (arredondando com duas casas decimais).
Veja aqui um exemplo:
Entrada:
804.36
Sa ́ıda:
38.30
'''

produto= float(input())
parc = produto/21
print(parc)
