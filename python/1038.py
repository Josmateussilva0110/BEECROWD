codi, amount = input().split()
codi = int(codi)
amount = int(amount)
if codi == 1:
    total = amount * 4.00
elif codi == 2:
    total = amount * 4.50
elif codi == 3:
    total = amount * 5.00
elif codi == 4:
    total = amount * 2.00
elif codi == 5:
    total = amount * 1.50
print(f'Total: R$ {total:.2f}')
