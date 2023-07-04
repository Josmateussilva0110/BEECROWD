while True:
    sun = 0
    a, b = map(int, input().split(' '))
    if a <= 0 or b <= 0:
        break
    if a > b:
        upper = a
        lower = b
    else:
        upper = b
        lower = a
    for i in range(lower, upper+1):
        print(i,end=' ')
        sun += i
    print(f'Sum={sun}')
