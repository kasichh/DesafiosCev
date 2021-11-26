print('Teste de financiamento de casas')
casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o valor do seu salário? '))
ano = int(input('Em quantos anos vai ser pago a casa? '))
mes = ano*12
# limite = sal*0.3
prestacao = casa/mes

print(f'Para este finaciamento, o valor mensal será de {prestacao:.2f} por mês')

if prestacao <= (sal*0.3):
    print('Parabéns, esse financiamento foi aprovado para você!')
else:
    print('Infelizmente esse impréstimo não pôde ser liberado para você.')
