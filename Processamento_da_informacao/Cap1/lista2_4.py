def entrada():
    global total
    total = int(input())

def process():
    global oz33, oz13, oz8, oz7, oz1
    oz33 = total//33
    oz13 = (total%33)//13
    oz8 = ((total%33)%13)//8
    oz7 = (((total%33)%13)%8)//7
    oz1 = ((((total%33)%13)%8)%7)//1

def saida():
    print(oz33, "JabuticabaCoin(s) de OZ$ 33")
    print(oz13, "JabuticabaCoin(s) de OZ$ 13")
    print(oz8, "JabuticabaCoin(s) de OZ$ 8")
    print(oz7, "JabuticabaCoin(s) de OZ$ 7")
    print(oz1, "JabuticabaCoin(s) de OZ$ 1")

entrada()
process()
saida()