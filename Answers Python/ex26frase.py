frase = input('\nDigite uma frase: ').strip()
print('A letra "a" aparece {} Vezes'.format(frase.lower().count('a')))
print('A letra "a" aparece a primeira vez na {} posicao'.format(frase.lower().find('a')))
print('A letra "a" aparece a ultima vez na {} posicao\n'.format(frase.lower().rfind('a')))
