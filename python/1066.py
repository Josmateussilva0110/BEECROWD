cont = cpar = cimpar = cposi = cnega = 0
while cont < 5:
    value = int(input())
    if value % 2 == 0:
        cpar += 1
    if value % 2 != 0:
        cimpar += 1
    if value > 0:
        cposi += 1
    if value < 0:
        cnega += 1
    cont +=1 
print(f'{cpar} valor(es) par(es)')
print(f'{cimpar} valor(es) impar(es)')
print(f'{cposi} valor(es) positivos(s)')
print(f'{cnega} valor(es) negativo(s)')
