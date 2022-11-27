from datetime import datetime

maior = 0
menor = 0

print("\nDigite a idade de 7 pessoas!")

for c in range (0,7):
    
    nasc = int(input("Idade da pessoa {}: ".format(c+1)))
    idade = int(datetime.today().year - nasc)

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print("Com isso, {} ainda sao de menor de idade, e {} ja sao de maior de idade.\n".format(menor, maior))

