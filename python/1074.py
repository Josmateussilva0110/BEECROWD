value = int(input())
for _ in range(value):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num <= 0 and num % 2 != 0:
        print('ODD NEGATIVE')
    elif num <= 0 and num % 2 == 0:
        print('EVEN NEGATIVE')
    elif num >= 0 and num % 2 != 0:
        print('ODD POSITIVE')
    elif num >= 0 and num % 2 == 0:
        print('EVEN POSITIVE')
