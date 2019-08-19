def remove_repetidos(lista):
    lista_or = lista[:1]
    for i in lista:
        for n in lista:
            if i in lista_or:
                pass
            else:
                lista_or.append(i)
    lista_or.sort()
    return lista_or
