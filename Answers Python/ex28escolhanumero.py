from random import randint

pcnum = randint(0, 5)
num = int(input('\nDescubra um numero que vai de 0 a 5: '))

if(num == pcnum):
    print('O numero informado foi {} e este e o numero certo, PARABENS :D\n'.format(pcnum))
else:
    print('O numero informado foi {} porem voce ERROUUU, o numero certo seria {} :(\n'.format(num,pcnum))