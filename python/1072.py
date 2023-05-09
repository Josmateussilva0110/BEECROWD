size = int(input())
cf = cd = 0
for i in range(size):
    value = int(input())
    if 10 <= value <= 20:
        cf += 1
    if value < 10 or value > 20:
        cd += 1
print(f'{cf} in')
print(f'{cd} out')
