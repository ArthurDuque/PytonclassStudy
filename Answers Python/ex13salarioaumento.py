salario = float(input('\nDigite o salario do funcionario: '))
aumento = float(input('Digite quantos % de aumento deseja: '))
print('Com o aumento de {}%, o salario do funcionario passa a ser: {:.2f} reais\n'.format(aumento, salario * (1+ (aumento/100))))

