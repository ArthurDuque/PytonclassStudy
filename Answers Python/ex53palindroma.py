frase = input("\nDigite algo, para verificacao de polindromo: ")
frase1 = ''.join(frase.split())

print("A frase informada: '{}'\n  E ao-contrario : '{}'".format(frase, frase1))

if (frase1[::-1] == ''.join(frase.split())):
    print("\n\t\tE igual, logo, ela e um palindromo :D\n")
else:
    print("\n\t\tE diferente, logo, ela NAO e um palindromo :C\n")
    