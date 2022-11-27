valor = float(input("\nQual o valor da casa: "))
salario = float(input("Salario: "))
anos = int(input("Anos: "))

mes = anos*12
prestacao = valor/mes
porce = salario*0.30

print("\n30 porcento do seu salario e R${:.2f} reais".format(porce))

if prestacao < porce:
    print("A casa no valor de R${:.2f} sera paga em {} meses, em prestacoes de R${:.2f} reais.".format(valor,mes,prestacao))
    print("Parabens voce pode fazer o emprestimo da casa.\n")
elif prestacao > porce:
    print("A casa no valor de R${:.2f} sera paga em {} meses, em prestacoes de R${:.2f} reais.".format(valor,mes,prestacao))
    print("Infelizmente foi negado a compra da casa, ja que as prestacoes ultrapassam o valor de 30% do seu salario.\n")
elif prestacao == porce:
    print("A casa no valor de R${:.2f} sera paga em {} meses, em prestacoes de R${:.2f} reais.".format(valor,mes,prestacao))
    print("Voce tem exatamente o que e necessario para parcelar a casa.\n")
else:
    print("Se e rico pra que parcelar\n")