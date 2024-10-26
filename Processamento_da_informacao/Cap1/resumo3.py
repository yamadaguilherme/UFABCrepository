#Escreva instruções para calulcar o delta utilizando a função "delta()", onde a função é dada por b * b - 4 * a * c, calcule para
# os valores de 5x^2 – 2x + 4

def delta( a, b, c ):
  d = b * b - 4 * a * c
  return d
valor = delta( 5, -2, 4)
print("O delta de 5x^2 – 2x + 4 é %.1f" % valor)