size = int(input())
for _ in range(size):
    x, y = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    else:
        ans = x / y
        print(f'{ans:.1f}')
