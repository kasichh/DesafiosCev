import math
print('-=' * 3, 'Calculador de hipotenusa', '=-' * 3)

c1 = float(input('Primeiro cateto: '))
c2 = float(input('Segundo cateto: '))
# hip = math.sqrt((c1**2 + c2**2))
hip = math.hypot(c1, c2)

print(f'Em um triangulo retangulo de catetos {c1} e {c2}, a hipotenusa vale: {hip}!')
print('-='*9)
