lista = list()
continua = 'x'
valor_novo = ''
while True:
    continua = 'x'
    valor_novo = int(input('Digite um valor: '))
    if valor_novo in lista:
        print('O valor digitado já foi adicionado. Não o adicionarei.')
    else:
        lista.append(valor_novo)
        print('Valor adicionado com sucesso!')
    while continua not in ('SN'):
        continua = str(input('Deseja continuar? [S/N]')).upper()[0]
    if continua == 'N':
        break
print(sorted(lista))
