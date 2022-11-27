print("\nDigite os dados de 4 pessoas pessoas!")

somaidade  = 0
mulher     = 0
homemvelho = 0
nomehomem  = 0

for c in range (0,4):
    nome  = input(" Nome da pessoa {}: ".format(c+1))
    idade = int(input("Idade da pessoa {}: ".format(c+1)))
    sexo  = input(" Sexo da pessoa {}: ".format(c+1))
    print()

    somaidade += idade

    if sexo == 'h' and idade > homemvelho:
        homemvelho = idade
        nomehomem  = nome
    elif sexo == 'm' and idade < 20:
        mulher += 1

print('''\nCom isso:
    A media das idades: {} anos.
    O homem mais velho: {} com {} anos.
Mulheres com < 20 anos: {}\n'''.format(somaidade/4, nomehomem, homemvelho, mulher))