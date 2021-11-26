from datetime import datetime


def voto(nasc):
    ano = datetime.now().year
    idade = ano-nasc
    if idade<16:
        print(f'Com {idade} anos, Não vota')
    elif idade<18:
        print(f'Com {idade}, voto opcional')
    elif idade<65:
        print(f'Com {idade} anos, voto obrigatório')
    else:
        print(f'Com {idade} anos, voto opcional')


voto(int(input('Digite o ano de nascimento: ')))