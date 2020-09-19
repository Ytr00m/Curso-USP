def menor_nome(nomes):
    menor = ""
    tam = 100000
    for i in nomes:
        i = i.strip()
        if len(i) < tam:
            menor = i.capitalize()
        tam = len(i)
    return menor
print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))