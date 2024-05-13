import random
continuar = "S"
Perro = 0 
Perro = 0
while continuar.upper()=="S": 
    ns = random.randint(1,10)
    T = 3
    while(T > 0):
        print ("você tem", T, "tentativas")
        T = T -1
        nc = int(input("Digite um número entre 1 e 10"))
        if ( ns == nc):
            print ("você acertou.")
            T = 0 
            Pcerto = Pcerto +1
        else:
            print("você errou")
            Perro = Perro +1
        print("número de acerto:", Pcerto)
        print("número de erros:", Perro)    
    continuar = input("deseja continuar? (s)im")            
