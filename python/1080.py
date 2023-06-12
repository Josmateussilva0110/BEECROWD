dados = list()
for _ in range(100):
    value = int(input())
    dados.append(value)
result = dados.index(max(dados))
print(f'{max(dados)}')
print(result+1)
