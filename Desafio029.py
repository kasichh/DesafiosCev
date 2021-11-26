v = int(input('RADAR - Fala a velo ai: '))

if v <= 80:
    print('Blz pode passar')
else:
    print('opa, passou')
    print(f'Vai pagar R$ {(v-80)*7:.2f} de multa')
