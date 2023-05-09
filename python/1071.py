x, y = map(int, input().split())
sun = 0
if x < y:
    maior = y
    menor = x
else:
    maior = x
    menor = y
for i in range(menor+1, maior):
    if i % 2 != 0:
        sun += i
print(f'{sun}')
