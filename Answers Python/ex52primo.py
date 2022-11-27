num = int(input(("\nDigite um numero inteiro: ")))


for n in range (0,1):
    if num == 2:
        print("O numero {} e primo :D\n".format(num))
    elif num%2 == 1 or num%3 == 1 or num%5 == 1 or num%7 == 1:
        print("O numero {} e primo :D\n".format(num))
    else:
        print("O numero {} NAO e primo :C\n".format(num))

