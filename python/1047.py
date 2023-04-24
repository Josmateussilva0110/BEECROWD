a, c, b, d = map(int, input().split())
duration = ((b * 60) + d) - ((a * 60) + c)
if duration <= 0:
    duration += (24 * 60)
print(f'O JOGO DUROU {duration//60} HORA(S) E {duration%60} MINUTO(S)')
