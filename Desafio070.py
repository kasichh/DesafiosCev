continua = 'S'
produto = ''
barato = str('')
preco = total_gasto = contagem = mais_de_mil = mais_barato = 0

while continua == 'S':
    produto = str(input('Qual o produto: '))
    preco = float(input('Valor do Produto: R$'))
    continua = 'X'
    while continua not in 'NS':
        continua = input('Deseja continuar? [S/N] ').strip().upper()

    total_gasto += preco
    if preco > 1000:
        mais_de_mil += 1
    if contagem == 0:
        barato = produto
        mais_barato = preco
    if preco < mais_barato:
        barato = produto
        mais_barato = preco
    contagem += 1

print('\nFim da compra!')
print(f'''Nesses {contagem} produtos:
O total da compra foi R${total_gasto}.
São {mais_de_mil} produtos mais caros que R$1000.00.
O produto mais barato foi {barato} e custou R${mais_barato}. ''')
