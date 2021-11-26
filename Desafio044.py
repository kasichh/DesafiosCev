preco = float(input('Digite preço normal do produto: '))
print('Digite a condicao de pagamento:\n'
      'A vista no dinheiro [1]\n'
      'A vista no cartão [2]\n'
      'Em 2x no cartão [3]\n'
      '3x ou mais no cartão [4]'
)
cond = str(input('Qual a opcão? ')).strip()

if cond == '1':
    print(f'Ficam R${preco*0.9:.2f} no dinheiro.')
elif cond == '2':
    print(f'Ficam R${preco*0.95:.2f} a vista no cartão.')
elif cond == '3':
    parcela = preco/2
    print(f'Ficam R${preco:.2f} em 2x de {parcela} no cartão.')
elif cond == '4':
    parc = int(input('Em Quantas parcelas? '))
    preco = preco * 1.2
    print(f'Ficam R${preco:.2f} em {parc}x de R${preco/parc:.2f} no cartão.')
else:
    print('Condição de pagamento não reconhecida.')
