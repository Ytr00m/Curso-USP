largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
count = 0
linha = 1
while count < altura:
    print("#" * largura)
    count += 1
    while linha < (altura-1):
        print("#", end = "")
        print(" " * (largura-2), end = "")
        print("#")
        linha += 1
    print("#" * largura)
    count += altura