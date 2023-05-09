q = int(input())
for _ in range(q):
    s = input().strip()
    pa = 0
    c = 0
    for p in s:
        if p == '<':
            pa += 1
        if p == '>' and pa > 0:
            pa -= 1
            c += 1
    print(c)
