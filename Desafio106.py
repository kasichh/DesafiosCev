import time
def sublinhar(texto):
    tamanho = len(texto)
    print('~'*(4+tamanho))
    print('  ' + texto)
    print('~'*(4+tamanho))


def ajuda():
    comando = 'x'
    while True:
        sublinhar('SISTEMA DE AJUDA PYHELP')
        comando = str(input('Digite o comando [fim para sair] > '))
        if comando.upper == 'FIM':
            break

        help(comando)
        time.sleep(3)




ajuda()
