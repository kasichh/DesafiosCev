num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

maior = num1

if num2 > maior:
    maior = num2

if num1 == num2:
    print('Os valores são iguais!')
elif num1 == maior:
    print('O PRIMEIRO valor é maior')
else:
    print('O SEGUNDO valor é maior')


# if num1 == num2:
#     print('Os valores são iguais!')
# elif num1 == maior:
#     print(f'O primeiro valor ({num1}) é maior')
#     print(f'O segundo valor ({num2}) é menor')
# else:
#     print(f'O segundo valor ({num2}) é maior')
#     print(f'O primeiro valor ({num1}) é menor')


# maior = max([num1, num2])
#
# if num1 == maior:
#     print('O primeiro valor é maior')
