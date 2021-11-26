print('='*20)
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser fatorado.
    :param show: (opcional) Mostrar conta.
    :return: O valor após fatorado.
    """
    i = 1
    for c in range(num, 0, -1):
        if show:
            if num == 1:
                print(num, end=' = ')
            else:
                print(num, end=' x ')
        i *= num
        num -= 1
    return i

print(fatorial(5, show=True))

help(fatorial)