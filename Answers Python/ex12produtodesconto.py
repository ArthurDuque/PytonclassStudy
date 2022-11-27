preco = float(input('\nDigite o preco do produto: '))
desc = float(input('Digite quantos % de desconto deseja: '))
print('Com o desconte de {}%, e preco do produto e: {:.2f} reais\n'.format(desc, preco*(1-(desc/100))))

