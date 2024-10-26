#Escreva instruções para converter a temperatura de "C" graus Celsius para Fahrenheit sabendo que temos que multiplicar C por 9/5 e depois somar 32.  O resultado deve ser armazenado na variável "F".

#Imprima o resultado da seguinte forma "xx graus Celsius corresponde a yy graus Fahrenheit".

#Note que a sequência  de instruções pede agora a LEITURA da variável C.

#Assim, se for lido o valor 65 para C, o resultado a ser exibido deve ser "65 graus Celsius corresponde a 149.0 graus Fahrenheit", se a variável C linda for igual a 65. 

C = int(input()) 
F = C * 9/5 + 32
print(C,"graus Celsius corresponde a", F, "graus Fahrenheit")
