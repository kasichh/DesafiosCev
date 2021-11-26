from datetime import date
ano = int(input('Digite o ano. Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
teste = ano % 4

if teste == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
