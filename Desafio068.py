import random
ganhou = jogadas = 1
computador = jogador = 0

print('Vamos jogar par ou impar!\n', '=-'*20)

while ganhou == 1:
    computador = random.randint(0, 5)
    jogador = int(input('\nEscolha um número: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()

    if escolha == 'I':
        print('OK eu fico com o par')
        print(f'Eu escolhi {computador}. ', end='')

        if (computador + jogador) % 2 == 0:
            print(f'O total de {computador + jogador} foi PAR')
            break
        else:
            print(f'O total de {computador + jogador} foi IMPAR')
    else:
        print('OK eu fico com o impar')
        print(f'Eu Escolhi {computador}. ', end ='')

        if (computador + jogador) % 2 == 0:
            print(f'O total de {computador + jogador} foi PAR')
        else:
            print(f'O total de {computador + jogador} foi  IMPAR')
            break
    print('\nVocê venceu!\nVamos jogar novamente!\n', '=-'*20)
    jogadas += 1
print('\n', '=-'*20)
print(f'Você perdeu. E jogou um total de {jogadas} vezes')