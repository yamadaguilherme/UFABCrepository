#Escreva um programa que ajude uma loja a fazer uma venda cujo pagamento  ́e parcelado. Assuma que a loja divide o
#pre ̧co em 21 parcelas iguais e sem quaisquer acr ́escimos (juros, multas, etc). Fa ̧ca programa que:
#• leia do teclado o pre ̧co do produto;
#• imprima quanto custar ́a cada parcela (arredondando com duas casas decimais).
#Veja aqui um exemplo:
#Entrada:
#804.36
#Sa ́ıda:
#38.30

produto= float(input())
parc = produto/21
print(parc)