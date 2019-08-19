n = 1
lista = []
while n != 0:
    n = int(input("Digite um número: "))
    lista.append(n)
print(" ")
lista.remove(0)
lista_inv = []
while len(lista) > 0:
    lista_inv.append(lista[-1])
    del lista[-1]
for i in lista_inv:
    print(i)