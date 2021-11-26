#desafio 098
import time
def contador(inicio, fim, passo):
    if passo == 0:
        if inicio>fim:
            passo = -1
        else:
            passo = 1
    if inicio > fim:
        if passo >0:
            passo = passo*-1
        fim = fim - 2
    print(f'Para o início em {inicio} até {fim} com passo de {passo} temos os valores: ')
    time.sleep(1)
    for c in range(inicio, fim+1, passo):
        print(c, end=' ')
        time.sleep(0.5)
    print('\n', '=-'*15)


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez!')
contador(int(input('inicio: ')), int(input('fim: ')), int(input('passo: ')))