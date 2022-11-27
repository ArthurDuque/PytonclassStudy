print("\nDigite 6 numeros inteiros!")

cont = 0

for n in range (0,6):
    num = int(input("Numero: "))
        
    if num%2 == 0:
        cont += num

print("A soma dos 6 numeros pares e: {}".format(cont))