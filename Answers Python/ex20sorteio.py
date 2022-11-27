from random import shuffle

a = input('\nDigite o nome do 1 aluno: ')
b = input('Digite o nome do 2 aluno: ')
c = input('Digite o nome do 3 aluno: ')
d = input('Digite o nome do 4 aluno: ')
l = [a , b, c, d]

shuffle(l)
print('A ordem de apresentacao e: ',l)

