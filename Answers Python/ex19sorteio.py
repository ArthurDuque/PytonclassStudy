from random import choice

a = input('\nDigite o nome do 1 aluno: ')
b = input('Digite o nome do 2 aluno: ')
c = input('Digite o nome do 3 aluno: ')
d = input('Digite o nome do 4 aluno: ')
l = [a , b, c, d]
print('O sorteado para apagar o quadro foi: {}\n'.format(choice(l)))
