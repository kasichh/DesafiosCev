def leia_dinheiro(texto):
    while True:
        valor = input(f'{texto}').replace(',', '.')
        numero = valor.replace('.', '')

        if numero.isnumeric():
            break
        else:
            print(f'ERRO "{valor}" não é um preço válido!')
    valor = float(valor)
    return valor
