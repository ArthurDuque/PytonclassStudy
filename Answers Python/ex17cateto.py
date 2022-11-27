from math import hypot

co = float(input('\nCateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('A hipotenusa e: {:.3f}\n'.format(hypot(co,ca)))
