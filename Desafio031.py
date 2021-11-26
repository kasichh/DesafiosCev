dist = int(input('Digite a distancia da viagem: '))

if dist <= 200:
    print(f'A viagem fica: R${dist*0.5}')
else:
    print(f'A viagem fica: R${dist*0.45}')
