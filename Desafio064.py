numero = soma = quantidade = 0

while numero != 999:
    numero = int(input('Digite um valor pra somar [999 para sair]: '))
    soma += numero
    quantidade += 1
print(f'A soma dos {quantidade-1} números é {soma-999}')
