ano = int(input('\nDigite o ano: '))
bis1 = ano % 4
bis2 = ano % 100
bis3 = ano % 400

if(bis1 == 0 and bis2 != 0 or bis3 == 0):
    print('O ano {} e um ano bissexto.\n'.format(ano))
else:
    print('O ano {} nao e um ano bissexto.\n'.format(ano))