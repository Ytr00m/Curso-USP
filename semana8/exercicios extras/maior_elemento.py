def maior_elemento(lista):
    imaior = 0
    for i in lista:
        for n in lista:
            if i >= n:
                imaior += 1
                if imaior == len(lista):
                    maior = i
    return maior