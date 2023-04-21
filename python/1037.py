value = float(input())
if value < 0 or value > 100.0:
    print('Fora de intervalo')
elif value <= 25.0:
    print('Intervalo [0,25]')
elif value <= 50.0:
    print('Intervalo (25,50]')
elif value <= 75.0:
    print('Intervalo (50,75]')
elif value <= 100.0:
    print('Intervalo (75,100]')
