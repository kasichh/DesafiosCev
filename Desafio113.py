def imprimir_valores(i, r):
    return f'O valor inteiro digitado foi {i} e o real foi {r}'


def leia_int():
    while True:
        try:
            inteiro = int(input('Digite um valor inteiro: '))
        except (ValueError, TypeError):
            print('Erro, valor digitado não é um inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o valor')
            return 0
        else:
            return inteiro


def leia_float():
    while True:
        try:
            real = float(input('Digite um real: '))
        except(ValueError, TypeError):
            print('Erro, valor digitado não é um real válido:')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o valor')
            return 0
        else:
            break
    return real


valor_inteiro = leia_int()
valor_real = leia_float()

print(imprimir_valores(valor_inteiro, valor_real))
