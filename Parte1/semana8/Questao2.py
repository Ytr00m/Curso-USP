def soma_elementos(lista):
    n = 1
    x = 0
    for i in lista:
        x += i
        if len(lista) > (n+1):
            n += 1
        else:
            pass
    return x
