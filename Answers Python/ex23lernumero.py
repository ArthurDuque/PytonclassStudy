num= input('Digite um numero entre 0 e 9.999: ')
print('O numero {} tem: {} milhares'.format(num, num[0]))
print('O numero {} tem: {} centenas'.format(num, num[1]))
print('O numero {} tem: {} dezenas'.format(num, num[2]))
print('O numero {} tem: {} unidades\n\n\n'.format(num, num[3]))
#erro ao digitar 4 numeros btw da pra fazer por laco



b = int(num)
print('O numero {} tem: {} milhares'.format(b,  b // 1000 ))
print('O numero {} tem: {} centenas'.format(b,  (b // 100) % 10 ))
print('O numero {} tem: {} dezenas'.format(b, (b // 10) % 10 ))
print('O numero {} tem: {} unidades'.format(b, (b // 1) % 10))
