N = int(input())
h = N // 60 ** 2
N = N - h * 60 ** 2
m = N // 60
N = N - m * 60
s = N
print(f'{h}:{m}:{s}')
