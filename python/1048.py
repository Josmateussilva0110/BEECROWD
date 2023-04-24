value = float(input())
if 0.0 <= value <= 400:
    readjust = value * 0.15
    new_wage = value + readjust
    percentage = 15
elif 400.01 <= value <= 800.00:
    readjust = value * 0.12
    new_wage = value + readjust
    percentage = 12
elif 800.01 <= value <= 1200.00:
    readjust = value * 0.10
    new_wage = value + readjust
    percentage = 10
elif 1200.01 <= value <= 2000.00:
    readjust = value * 0.07
    new_wage = value + readjust
    percentage = 7
else:
    readjust = value * 0.04
    new_wage = value + readjust
    percentage = 4
print(f'Novo salario: {new_wage:.2f}')
print(f'Reajuste ganho: {readjust:.2f}')
print(f'Em percentual: {percentage} %')
