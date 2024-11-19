def entrada():
    global f, e, y 
    f = int(input())
    e = int(input())
    y = int(input())
    
def vox(f, e, y):
    global vox
    vox1 = (f * (e**2) * (y**3))/(f+e+y)
    vox = "%.2f" % vox1
    return vox

def saida():
    print("vox = ", vox)
    
entrada()
vox(f, e, y)
saida()