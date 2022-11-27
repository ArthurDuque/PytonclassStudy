print("\nSoma impares de 1 a 500:")

cont = 0
for num in range(1, 500, 2):
    if num%3 == 0:
        cont += num
print('A Soma e: {} :D\n'.format(cont))