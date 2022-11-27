peso = float(input('\nDigite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso/(altura**2)

if (imc >= 1) and (imc < 18.5):
    print("O seu IMC e {:.1f}, logo, voce esta ABAIXO DO PESO!\n".format(imc))
elif (imc >= 18.5) and (imc < 25):
    print("O seu IMC e {:.1f}, logo, voce esta no PESO IDEAL!\n".format(imc))
elif (imc >= 25) and (imc < 30):
    print("O seu IMC e {:.1f}, logo, voce esta com SOBREPESO!\n".format(imc))
elif (imc >= 30) and (imc < 40):
    print("O seu IMC e {:.1f}, logo, voce esta com OBESIDADE!\n".format(imc))
elif imc >= 40:
    print("O seu IMC e {:.1f}, logo, voce esta com OBESIDADE MORBIDA!, se vai more.\n".format(imc))
else:
    print("Dados inconsistentes, favor redigita-los.\n")
