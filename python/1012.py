a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
triangulo = (a * c) / 2
circulo = pi * (c ** 2) 
tra = (a + b) * c
trapezio = tra / 2
quadrado = b * b
retangulo = a * b
print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
