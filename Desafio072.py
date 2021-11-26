numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'desseseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print('Digite um numero pra eu digitar ele por extenso[0 - 20]: ')
while True:
    numero = int(input())
    if -1 < numero < 21:
        break
    else:
        print('Digite um número válido 0 - 20, tente novamente: ')


print(f'Você digitou o número {numero_extenso[numero]}')

