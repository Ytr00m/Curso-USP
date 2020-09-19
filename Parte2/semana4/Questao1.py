def ordenada(lista):

    elementoAnterior = lista[0]
    ordenados = 0

    for i in range(len(lista)):

        if lista[i] >= elementoAnterior:
            ordenados += 1

        elementoAnterior = lista[i]

    if ordenados == len(lista):

        return True

    else:
        
        return False
