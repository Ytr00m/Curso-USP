def imprime_matriz(matriz):
    for i in matriz:
        for j in i:
            if j == i[-1]:
                print(j, end="")
            else:
                print(j, end=" ")
        print("")
