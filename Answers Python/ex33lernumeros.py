num1 = input('Digite o 1 numero: ')
num2 = input('Digite o 2 numero: ')
num3 = input('Digite o 3 numero: ')

maior = num1
if(num1 < num2 and num3 < num2):
    maior = num2
if(num1 < num3 and num2 < num3):
    maior = num3

menor = num1
if(num1 > num2 and num3 > num2):
    menor = num2
if(num1 > num3 and num2 > num3):
    menor = num3


print('maior {}'.format(maior))
print('menor {}'.format(menor))