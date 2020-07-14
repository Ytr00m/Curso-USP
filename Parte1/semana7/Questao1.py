largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
count = 0
linha = 0
while count < altura:
    while linha < largura:
        print("#", end = "" )
        linha += 1
    print("")
    linha = 0
    count += 1
    
