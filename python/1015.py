import math

def distancia(x1, y1, x2, y2):
    soma1 = x1 - x2
    soma2 = y1 - y2
    mult1 = soma1 * soma1
    mult2 = soma2 * soma2
    soma3 = mult1 + mult2
    result = math.pow(soma3, 1/2)
    return result


x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)
x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)
result = distancia(x1, y1, x2, y2)
print(f'{result:.4f}')
