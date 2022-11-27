reta1 = float((input('Digite o comprimento da 1 reta: ')))
reta2 = float((input('Digite o comprimento da 2 reta: ')))
reta3 = float((input('Digite o comprimento da 3 reta: ')))

if (reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta2+reta3):
    print('E possivel formar um triangulo, que legal.\n')
else:
    print('NAO e possivel formar um triangulo, tente novamente.\n')