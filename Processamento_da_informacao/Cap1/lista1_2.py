#Fa ̧ca um programa para calcular e imprimir o valor da express ̃ao (f ́ormula) abaixo, a partir das vari ́aveis reais D e I. As
#vari ́aveis D e I devem ser lidas do teclado, nessa ordem.
#K = (raiz(D^2 + I^2))/5DI
#Mostrar o resultado, com trˆes casas decimais, conforme exemplo a seguir:
#Entradas:
#8.400
#5.300
#Sa ́ıda:
#K = 0.045

D = float(input())
I = float(input())
K= (D**2 + I**2) **(0.5)/(5*D*I)
print("K =" "%.3f" % K)