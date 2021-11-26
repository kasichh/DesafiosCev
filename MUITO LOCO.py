qtd = 0
num = int(input('Digite um número: '))

while True:
    if num % 2 == 0:
        num /= 2
    elif num > 0:
        num = (num*3)+1
    else:
        num = (num*3)-1
    qtd += 1
    print(f'O {qtd} numero é {num}')
    if num == 1:
        break
    if num == -1:
        break