from random import randint

pcnum = randint(0, 10)
num = 0
erro = 0

while num != pcnum:
    num = int(input('Descubra um numero que vai de 0 a 10: '))

    if num != pcnum:
        print('Voce informou o numero {} porem voce ERROUUU :(\n'.format(num))
        erro += 1
    if num == pcnum:
        print('Voce informou o numero {} e este e o numero certo, PARABENS :D'.format(pcnum))
print('Foram dados ao todo {} palpites ate a vitoria\n'.format(erro))