cont = sun = 0
while True:
    if cont == 2:
        break
    a = float(input())
    if 0 <= a <= 10:
        cont += 1
        sun += a
    else:
        print('nota invalida')
ans = sun / 2
print(f'media = {ans:.2f}')
