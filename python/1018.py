n = int(input())
print(n)
ce = n // 100
n = n - ce * 100
ci = n // 50
n = n - ci * 50
vin = n // 20
n = n - vin * 20
dez = n // 10
n = n - dez * 10
cin = n // 5
n = n - cin * 5
dois = n // 2
n = n - dois * 2
um = n // 1
n = n - um * 1
print(f'{ce} nota(s) de R$ 100,00')
print(f'{ci} nota(s) de R$ 50,00')
print(f'{vin} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cin} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')
