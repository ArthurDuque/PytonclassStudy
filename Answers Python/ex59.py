from os import system

valor1 = 0
valor2 = 0
opcao = 1

while opcao != 5:
    opcao = int(input('''\nEscolha uma opcao:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do programa
    \t\t\t\t'''))
    
    if opcao == 1:
        system('clear')
        print("A soma dos numeros {} + {} e {}".format(valor1, valor2, valor1+valor2))
    elif opcao == 2:
        system('clear')
        print("A multiplicar dos numeros {} + {} e {}".format(valor1, valor2, valor1*valor2))
    elif opcao == 3:
        if valor1 > valor2:
            system('clear')
            print("Entre dos numeros {} e {} o maior e {}".format(valor1, valor2, valor1))
        else:
            system('clear')
            print("Entre dos numeros {} e {} o maior e {}".format(valor1, valor2, valor2))
    elif opcao == 4:
        print("Digite 2 numeros:")
        valor1 = float(input('Numero 1: '))
        valor2 = float(input('Numero 2: '))
        system('clear')
