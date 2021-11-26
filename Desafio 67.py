t = 0
while True:
    t = int(input('Quer ver a tabuada de que valor?: '))
    print('=-'*20)
    if t > 0:
        for i in range(1,11):
            print(f'{t} x {i:2} = {t*i}')
    else:
        break
    print('=-'*20)
print('Programa encerrado')
