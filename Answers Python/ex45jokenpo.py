from random import randint

pessoa = int(input("\nDigite o nome da sua opcao: \n0 - Pedra\n1 - Papel\n2 - Tesoura\n\t\t\t"))

#["Pedra", "Papel", "Tesoura"]
comp = randint(0,2)

if pessoa == comp:
     print("Eh... deu EMPATE :P\n")
elif pessoa == 0:
    if comp == 1:
        print("Infelizmente voce PERDEU :C\n")
    else:
        print("Que legal voce GANHOU :D\n")
elif pessoa == 1:
    if comp == 0:   
        print("Que legal voce GANHOU :D\n")
    else:
        print("Infelizmente voce PERDEU :C\n")
elif pessoa == 2:
    if comp == 0:    
        print("Infelizmente voce PERDEU :C\n")
    else:
        print("Que legal voce GANHOU :D\n")
else:
    print("Opcao Invalida!!!\n")
    