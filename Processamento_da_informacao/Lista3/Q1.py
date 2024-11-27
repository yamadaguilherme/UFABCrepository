'''
Triangulos sao classificados da seguinte maneira:
• triangulo agudo, quando todos os angulos internos sao menores que 90;
• triangulo retangulo, quando o maior angulo interno e 90;
• triangulo obtuso, quando o maior angulo interno e maior do que 90.
E facil decidir o tipo de um triangulo analisando os seus lados. Suponha que os lados de um triangulo sejam  a, b, c com
c sendo o maior dos lados.
'''

def entrada():
    global a, b, c
    a = int(input())
    b = int(input())
    c = int(input())
    
def process():
    global f
    if a**2 + b**2 > c**2:
        f = "A"
    elif a**2 + b**2 == c**2:
        f = "R"
    else:
        f = "O"

def saida():
    print(f)

entrada()
process()
saida()