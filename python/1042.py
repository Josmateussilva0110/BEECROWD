x = input().split()
n1, n2, n3 = x
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        meio = n2
        menor = n3
    else:
        meio = n3
        menor = n2
if n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        meio = n1
        menor = n3
    else:
        meio = n3
        menor = n1
if n3 > n1 and n3 > n2:
    maior = n3
    if n1 > n2:
        meio = n1
        menor = n2
    else:
        meio = n2
        menor = n1
print(f'{menor}\n{meio}\n{maior}')
print()
print(f'{n1}\n{n2}\n{n3}')
