nome = input('Digite um nome: ')

print('O nome em maiusculo: {}'.format(nome.upper()))
print('O nome em minusculo: {}'.format(nome.lower()))
print('O nome tem {} letras sem contar os espacos'.format(len(''.join(nome.split()))))
print('O primeiro nome possui {} letras'.format(len(nome.split() [0])))