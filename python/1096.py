i = 1
j = 7
t = r = 0
while t != 3 and r != 3:
    print(f'I={i} J={j}')
    j -= 1
    t += 1
    if i == 9:
        r += 1
    if t == 3:
        i += 2
        j = 7
        t = 0
