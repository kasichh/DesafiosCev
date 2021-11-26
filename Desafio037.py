num = int(input('Digite um número: '))
c = str(input('Quer converter o número para:\n[1] para binário\n[2] para octal\n[3] para hexadecimal\n'))
t = c.strip()

if t == '1':
    print(f'Para binário, o numero {num} fica: {num:08b}')
elif t == '2':
    oc = oct(num)
    stoc = str(oc)
    print(f'Para octal, o numero {num} fica: {stoc[2:]}')
elif t == '3':
    he = hex(num)
    sthe = str(he)
    print(f'Para hexadecimal, o numero {num} fica: {sthe[2:]}')
else:
    print('Conversão não compreendida.')
