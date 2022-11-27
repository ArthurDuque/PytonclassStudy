kmp = float(input('\nForam rodados quantos km: '))
dias = int(input('A quantos dias o carro esta alugado: '))
a = kmp * 60
b = dias * 0.15
print('O carro custou no total {} reais, sendo {} reais pelos dias usados, e {} reais pelos km rodados\n'.format(a + b, a, b))
