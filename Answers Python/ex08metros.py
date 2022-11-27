a = int(input('\nDigite os metros: '))
print('Voce informou {} metro(s), este valor e igual a: '.format(a))
print('{} Kilometros\n{} Hectometros\n{} Decametro\n{} Metro\n{} Decimetro\n{} centimetros\n{} milimetros\n'.format(a/1000, a/100, a/10, a, a*10, a*100, a*1000))
