expressao = str(input('Digite uma expressão: '))
parenteses = 0

for c in expressao:
    if c == '(':
        parenteses += 1
    if c == ')':
        parenteses -= 1
    if parenteses < 0:
        break

if parenteses == 0:
    print('Sua expressão está correta!')
else:
    print('sua expressão está incorreta!')