from ex108 import moeda


n = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(n, "US$")} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.reduzir(n, 13))}')
