def fatorial(num, show=False):
    i = 1
    print('='*20)
    for c in range(num, 0, -1):
        if show:
            if num == 1:
                print(num, end=' = ')
            else:
                print(num, end=' x ')
        i *= num
        num -= 1
    print(i)

fatorial(5, show=True)