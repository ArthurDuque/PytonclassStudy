preco = float(input("\nDigite o preco do produto: "))
condi = int(input("Condicao de pagamento: \n1 - Dinheiro/Cheque + 10% Desconto\n2 - Cartao\n\t\t\t\t\t\t"))

if condi == 1:
    print("Pagamento no cheque/dinheiro a vista, o produto de R${} reais sai por R${} reais.\n".format(preco,preco*0.90))
elif condi == 2:
    condi = float(input("Opcoes de pagamento por cartao: \n1 - A vista no cartao + 5% Desconto\n2 - 2x no cartao + sem desconto\n3 - 3x ou mais no cartao + juros de 20%\n\t\t\t\t\t\t"))
    if condi == 1:
        print("Pagamento no cartao a vista, o produto de R${} reais sai por R${} reais.\n".format(preco,preco*0.95))
    elif condi == 2:
        print("Pagamento no cartao em 2x, o produto mantem seu preco sem desconto de R${} reais.\n".format(preco))
    elif condi == 3:
        print("Pagamento no cartao em 3x ou mais, o produto de R${} reais sai por R${} reais.\n".format(preco,preco*1.20))
    else:
        print("Opcao invalida!!!\n")
else:
    print("Opcao invalida!!!\n")

