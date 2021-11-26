numero = int(input('Digite o número a analisar: '))

unidade = numero%10
dezena = (numero%100-unidade)/10
centena = (numero%1000-(unidade+(dezena*10)))/100
milhar = (numero - (unidade + dezena*10 + centena*100))/1000


print(f'A unidade é: {unidade}')
print(f'A dezena é: {dezena:.0f}')
print(f'A centena é: {centena:.0f}')
print(f'O milhar é: {milhar:.0f}')
