#desafio 096
def area(l, c):
    area_total = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {area_total:.1f}m2.')


print('Controle de terrenos\n', '-'*20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
