sal = float(input('\nDigite o salario: '))

if(sal <= 1250):
    print('O salario tera um aumento de 15%, logo o novo valor e: {:.2f} reais\n'.format(sal*1.15))
else:
    print('O salario tera um aumento de 10%, logo o novo valor e: {:.2f} reais\n'.format(sal*1.1))
