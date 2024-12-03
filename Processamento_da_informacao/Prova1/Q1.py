def entrada():
    global x,y,xc,yc
    x = 4
    y = 57
    xc = 0
    yc = 0
def process():
    global xc,yc
    while x != xc or y != yc:
        xc = int(input())
        yc = int(input())
        if x != xc or y != yc:
            print("Errou")
def saida():
    print("Acertou")
entrada()
process()
saida()