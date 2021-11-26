print('Sequencia de fibonacci: ')

a = 1
b = 0
qnt = int(input('Quantos numeros voce quer terelteltel? '))

if (qnt%2 == 0):
    qnt = qnt//2
else:
    qnt = (qnt/2)+0.5
qnt = int(qnt)

for c in range(0, qnt):
    print(b)
    a = a + b
    if c != qnt - 1:
        print(a)
        b = a + b
