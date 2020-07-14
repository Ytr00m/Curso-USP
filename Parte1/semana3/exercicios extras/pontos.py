from math import sqrt
x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))
if sqrt(((x1 - x2) **2) + ((y1 - y2) ** 2)) >= 10:
    print("longe")
else:
    print("perto")    
