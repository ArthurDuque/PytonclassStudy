from datetime import datetime

nasc = int(input("\nDigite seu ano de nascimento: "))
idade = int(datetime.today().year - nasc)
sexo = int(input("Informe o sexo: \n1 - Homem\n2 - Mulher\n\t\t\t\t"))

if sexo == 1:
    if idade < 18:
        print("Voce tem {} anos, e voce ainda vai se alistar dentro de {} anos.\n".format(idade,18 - idade))
    elif idade == 18:
        print("Voce tem {} anos, e esta na hora de se alistar.\n".format(idade))
    else:
        print("Voce tem {} anos, e ja pode se alistar a {} anos.\n".format(idade,idade - 18))
else:
    print("Voce e mulher, e nao tem servico militar obrigatorio\n")