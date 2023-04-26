cont = soma = 0
for _ in range(6):
    value = float(input())
    if value > 0:
        cont += 1
        soma += value
        average = soma / cont
print(f'{cont} valores positivos')
print(f'{average:.1f}')
