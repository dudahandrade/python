def forca(tentativa):
    f1 = "  +--------+  "
    f2 = "  |           "
    f3 = "  |           "
    f4 = "  |           "
    f5 = "  |           "
    f6 = "  |           "
    f7 = "__|___________"

    if tentativa>= 1:
        f2="  |         | "
    if tentativa>= 2:
        f3="  |         o "
    if tentativa>= 3:
        f4="  |         | "
    if tentativa>= 4:
        f4="  |        /| " 
    if tentativa>=5:
        f4="  |        /|\ "     
    if tentativa>=6:
        f5="  |         |"  
    if tentativa>=7:
        f6="  |        /   "
    if tentativa>=8:  
        f6="  |        / \ "  

    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)


def continua():
    while True:
        print("-" * 20 )
        novamente = input("Quer jogar de novo S/N: "). upper()
        if novamente == "S":
            acabou = True
            break
        elif novamente == "N":
            acabou = False
            break
        else:
            print("Digite S ou N ")
    return acabou

def apresentapalavra(letras,palavras):
    npalavra="_ "*len(palavras)
    for l in range(0,len(letras)):
        print(letras[l])
        for p in range(0,len(palavras)):
            print(palavras[p])
            if letras[l]==palavras[p]:
                print(letras[l])
                print(l)
                print(p)
    return npalavra

def sorteiapalavra ():
    lista = ["amor","paz","prosperidade","ajuda","salvação"]
    return random.choice (lista)
     
##jogar = True
##x=0
##while jogar :
    ##print(x)
    ##forca(x)
    ##jogar = continua()
forca(0)


import random
print(sorteiapalavra())

print(apresentapalavra("ab","amor"))
