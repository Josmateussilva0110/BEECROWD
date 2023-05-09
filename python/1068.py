while True:
    try:
        lista = input().strip()
        cont = 0
        ver = True
        for p in lista:
            if p == '(':
                cont += 1
            elif p == ')':
                if cont > 0:
                    cont -= 1
                else:
                    ver = False
                    break
        if ver == True and cont == 0:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break
