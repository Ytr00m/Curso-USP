import random

def lista_grande(n):

    lista = []
    
    for i in range(n):

        lista.append(random.randint(n, 100000))

    return lista
