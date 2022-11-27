nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

print('A sua nota media e {}'.format(media))
if media < 5:
    print("A sua media {} esta abaixo de 5, logo voce foi REPROVADO!\n".format(media))
elif media >= 5 and media <= 6.9:
    print("A sua media {} esta abaixo de 7, logo voce esta de RECUPERACAO!\n".format(media))
else:
    print("A sua media {} esta acima de 6,9, logo voce esta APROVADO!\n".format(media))
