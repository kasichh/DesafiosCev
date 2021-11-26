from time import sleep
resultado = 0
escolha = 0

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

while escolha != '5':

    print('''
    Digite a operação:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    escolha = str(input('Digite ')).strip()

    if escolha == '1':
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}')
    elif escolha == '2':
        resultado = n1 * n2
        print(f'{n1} x {n2} = {n1*n2}')
    elif escolha == '3':
        resultado = n1
        if n2 > n1:
            resultado = n2
        print(f'Entre {n1} e {n2}, o maior valor vale: {resultado}')
    elif escolha == '4':
        print('Escolha novamente os números: ')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif escolha == '5':
        print('Finalizando...')
    else:
        print('Opção inválida, escolha novamente!')
    sleep(2)
    print('\n', '=-'*20)
print('\nO programa foi finalizado com sucesso!')
