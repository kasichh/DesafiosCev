r1 =  float(input('Digite o valor das retas: '))
r2 = float(input())
r3 = float(input())

maior = max(r1, r2, r3)

if maior == r1:
    if (r2 + r3) < r1:
        print('Não rola nada de triangulo!')
    else:
        print('É possivel fazer um triangulo.')
elif maior == r2:
    if (r1 + r3) < r2:
        print('Não rola nada de triangulo!')
    else:
        print('É possivel fazer um triangulo.')
else:
    if (r1 + r2) < r3:
        print('Não rola nada de triangulo!')
    else:
        print('É possivel fazer um triangulo.')
