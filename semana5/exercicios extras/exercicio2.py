from math import sqrt
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b ** 2 - 4 * a * c 

if delta == 0:
    def raiz1():
        return (-b + sqrt(delta))  / (2 * a)
    raiz1 = raiz1()
    print("A raiz desta equação é " + str(raiz1))
else: 
    if delta < 0:
        print("Esta equação não possui raizes reais.")
    else:
        def raiz1():
            return (-b + sqrt(delta))  / (2 * a)
        def raiz2():
            return (-b - sqrt(delta))  / (2 * a)
        raiz1 = raiz1()
        raiz2 = raiz2()
        if raiz1() < raiz2():
            print("As raizes desta equação são " + str(raiz1) + " e " + str(raiz2))
        else:
            print("As raizes desta equação são " + str(raiz2) + " e " + str(raiz1))