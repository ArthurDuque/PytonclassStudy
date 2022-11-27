dist = int(input('\nDigite a distancia da viagem em Km: '))

if(dist <= 200):
    print('Como a viagem tem menos de 200km, sera cobrado R$0,50 por Km rodado.')
    print('Logo o valor da viagem e de R${}'.format(dist*0.50))
else:
    print('Como a viagem tem mais de 200km, sera cobrado R$0,45 por Km rodado.')
    print('Logo o valor da viagem e de R${}'.format(dist*0.45))
print('Viacao geomax pro seu dIa mais feliz :D\n')


