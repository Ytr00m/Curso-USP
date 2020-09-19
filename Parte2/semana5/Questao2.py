def bubble_sort(lista):
    fim = len(lista)
    for i in range(fim-1, 0, -1):
        for k in range(i):
            if lista[k] > lista[k+1]:
                lista[k], lista[k+1] = lista[k+1], lista[k]
                print(lista)
    return lista