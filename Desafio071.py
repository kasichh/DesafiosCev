valor = int(input('Qual o valor a ser sacado? R$'))

cinquenta = valor//50
valor = valor % 50
vinte = valor//20
valor = valor % 20
dez = valor//10
valor %= 10
um = valor // 1

print('='*40)
print(f'''Foram sacadas:
{cinquenta} cédulas de R$ 50;
{vinte} cédulas de R$ 20;
{dez} cédulas de R$ 10;
{um} cédulas de R$ 1.''')
print('='*40)
print('Fim do programa')
