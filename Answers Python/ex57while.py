c = str(input("\nDigite seu sexo (M/F): ")).upper()

while c not in 'MF':
    c = str(input("Erro, use M- Masculino ou F- Feminino): "))
    
    if c in 'MF':
        print(':D')