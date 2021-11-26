t1 = int(input('Digite os valores dos lados do triangulo:\n'))
t2 = int(input())
t3 = int(input())

a = [t1, t2, t3]
a = sorted(a)

if a[2] >= (a[1] + a[0]):
    print('Não é possivel fazer um triangulo com esses lados.')
else:
    print('Esses valore podem formar um triangulo, sera um triangulo: ', end= '')
    if t1 == t2 and t2 == t3:
        print('Triangulo Equilátero.')
    elif t1 == t2 or t2 == t3 or t3 == t1:
        print('Triangulo Isóceles.')
    else:
        print('Triangulo Escaleno')
