#Escreva um programa para ler duas notas reais, calcular a média das duas notas e atribui um conceito:
# Onde: Média >= 9, Conceito A
# Onde: Média >= 7.5, Conceito B
# Onde: Média >= 6, Conceito C
# Onde: Média >= 5, Conceito D
# Onde: Média < 5, Reprovado! Conceito F

def leia():
  a = float(input("Digite a 1a nota: "))
  b = float(input("Digite a 2a nota: "))
  return a, b;
nota1, nota2 = leia()
media = (nota1 + nota2)/2
if media >= 9:  
  print("Conceito A")
elif media >= 7.5:  
  print("Conceito B");
elif media >= 6: 
  print("Conceito C")
elif media >= 5: 
  print("Conceito D")
else: 
  print("Reprovado! Conceito F")