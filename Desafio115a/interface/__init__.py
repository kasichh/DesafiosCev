import time
from time import sleep


len_carac = 45


def print_linha():
    print('-' * len_carac)


def menu_principal():
    print_linha()
    print(f'{"Menu Principal":^{len_carac}}')
    print_linha()
    print(
        f'''{"1 - Ver pessoas cadastradas":<{len_carac}}\n{"2 - Cadastrar nova pessoa":<{len_carac}}\n{"3 - Sair do sistema":<{len_carac}}'''
    )
    print_linha()
    escolha = int(input('Sua opção: '))
    return escolha


def main():
    escolha = 'x'
    while escolha not in [1, 2, 3]:
        escolha = menu_principal()
        try:
            int(escolha)
        except(ValueError, TypeError):
            print('Digite um valor válido')
        if escolha not in [1, 2, 3]:
            print('Digite um valor dentro dos valores válidos do menu')
            time.sleep(1)
    if escolha == 1:

    if escolha == 3:
        quit()


if __name__ == '__main__':
    while True:
        main()