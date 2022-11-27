vel = float(input('\nInforme a velocidade do meliante: '))
limite = float(input('Informe a velocidade permitida da via: '))

if(vel > limite):
    print('{:.2f}Km/h esta acima do limite permitido de {:.2f}Km/h!!!'.format(vel,limite))
    print('Sera gerado uma multa no valor de R${:.2f} reais.\n'.format(7*(vel-limite)))
else:
    print('{:.2f}Km/h esta dentro limite permitido de {:.2f}}Km/h!!!\n'.format(vel,limite))




