reta1 = float((input('\nDigite o comprimento da 1 reta: ')))
reta2 = float((input('Digite o comprimento da 2 reta: ')))
reta3 = float((input('Digite o comprimento da 3 reta: ')))

if (reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta2+reta3):
    print('\nE possivel formar um triangulo, que legal :D')
    if reta1 == reta2 == reta3:
        print("Ja o tipo do triangulo formado sendo Equilatero\n")
    elif reta1 != reta2 != reta3:
        print("Ja o tipo do triangulo formado sendo Escaleno\n")
    else:
        print("Ja o tipo do triangulo formado sendo Isoseles\n")
else:
    print('NAO e possivel formar um triangulo, tente novamente :C\n')