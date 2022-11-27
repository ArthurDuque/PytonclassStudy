num = int(input("\nDigite um numero inteiro qualquer: "))
resp = int(input("Digite qual vai ser a base de conversao, sendo:\n1 - Binario\n2 - Octal\n3 - Hexadecimal\n\t\t\tOpcao: "))

if resp == 1:
    bin = format(num, "b")
    print("O numero inteiro {} em Binario e {}.\n".format(num,bin))
elif resp == 2:
    oct = format(num, "o")
    print("O numero inteiro {} em Octal e {}.\n".format(num,oct))
elif resp == 3:
    hex = format(num, "x")
    print("O numero inteiro {} em Hexadecimal e {}.\n".format(num,hex))
else:
    print("Numero selecionado invalido.\n")