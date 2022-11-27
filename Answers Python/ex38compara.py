num1 = int(input("\nDigite o 1 numero inteiro: "))
num2 = int(input("Digite o 2 numero inteiro: "))

if num1 > num2:
    print("O primeiro numero {} e o maior.\n".format(num1))
elif num1 < num2:
    print("O segundo numero {} e o maior.\n".format(num2))
else:
    print("Os numeros sao iguais, nao existe valor maior.\n")
