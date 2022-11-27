num = 1
num1 = 0
contador = 0
print()

while num != 999:
    num = int(input('Digite um numero: '))
    num1 += num
    contador += 1

print('Programa finalizado,')
print('Foram digitados {} numeros e a soma destes numeros e {}.\n'.format(contador-1, num1-999))
