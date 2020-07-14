n = int(input("Digite um numero inteiro: "))
anterior = n % 10
n = n // 10
adj_iguais = False
while n > 0 and not adj_iguais:
    atual = n % 10
    if atual == anterior:
        adj_iguais = True
    else:
        anterior = atual
        n = n // 10
if adj_iguais == True:
    print("sim")
else:
    print("não")