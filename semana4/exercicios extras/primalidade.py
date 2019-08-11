n = int(input("Digite um numero inteiro: "))
ehprimo = True
divisor = 2
while divisor < n and ehprimo:
    if n % divisor == 0:
        ehprimo = False
    divisor += 1
if ehprimo and n != 1:
    print("primo")
else:
    print("não primo")