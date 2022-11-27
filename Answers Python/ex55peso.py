print("\nDigite o peso de 5 pessoas!")

menosp = 1000
maisp = 0

for c in range (0,6):
    peso = int(input("Peso da pessoa {}: ".format(c+1)))

    if peso > maisp:
        maisp = peso
    elif peso < menosp:
        menosp = peso

print("Com isso, o maior peso foi {}, e o menor foi {}.\n".format(maisp, menosp))