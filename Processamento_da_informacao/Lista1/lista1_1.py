'''
Considere as instrucoes abaixo:
   inteiro distancia = 20, KM Inicial = 19.76 , KM Final
   ler (KM Final )
   distancia = KM Final - KM Inicial
   escreva ( distancia )
Se KM Final for uma variavel de entrada, qual  ́e a distancia impressa (considerando o valor lido em KM Final)? Para
responder, faca um programa que reproduza as instrucoes acima. Aqui um exemplo de como seria entrada e a saıda desse
programa:
Entrada:
201.46
Saıda:
distancia = 181.70
Atencao: a saıda deve ter exatamente a mesma formatação desse exemplo acima.
'''

KM_inicial = 19.76
KM_final = float(input())
distancia = KM_final - KM_inicial
print("distancia =" "%.2f" % distancia)
