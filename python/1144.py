n = int(input())
for i in range(1, n+1):
    tot = i* i
    tot2 = i * tot
    print(f'{i} {tot} {tot2}')
    print(f'{i} {tot+1} {tot2+1}')
