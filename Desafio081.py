lista = list()
continua = 'x'
contagem = cinco = 0

while True:
    lista.append(int(input('Digite um número: ')))

    continua = 'x'
    while continua not in 'SN':
        continua = str(input('Deseja continuar?[S/N]')).upper().strip()[0]

    contagem += 1

    if continua == 'N':
        break
print('=-'*10)
print(f'A lista digitada foi {lista}')
print(f'Foram digitados {contagem} números')
arrumado = lista[:]
arrumado.sort(reverse=True)
print(f'De forma decrescente, fica: {arrumado}')
if 5 in lista:
    print('O valor 5 foi digitado na lista')
else:
    print('O valor 5 não foi digitado na lista.')