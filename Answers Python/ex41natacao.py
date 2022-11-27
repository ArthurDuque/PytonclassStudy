from datetime import datetime

nasc = int(input("\nDigite seu ano de nascimento do atleta: "))

ano = int(datetime.today().year)
idade = ano - nasc

if idade <= 9:
    print("Voce tem {} anos, logo, voce esta na categoria MIRIM.\n".format(idade))
elif idade <= 14:
    print("Voce tem {} anos, logo, voce esta na categoria INFANTIL.\n".format(idade))
elif idade <= 19:
    print("Voce tem {} anos, logo, voce esta na categoria JUNIOR.\n".format(idade))
elif idade <= 25:
    print("Voce tem {} anos, logo, voce esta na categoria SENIOR.\n".format(idade))
else:
    print("Voce tem {} anos, logo, voce esta na categoria MASTER.\n".format(idade))

