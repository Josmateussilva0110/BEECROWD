start, end = map(int, input().split())
while start < 0 or end < 0:
    start, end = map(int, input().split())
if start >= end:
    duration = 24 - start + end
    print(f'O JOGO DUROU {duration} HORA(S)')
else:
    duration = end - start 
    print(f'O JOGO DUROU {duration} HORA(S)')
