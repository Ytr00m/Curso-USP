n = int(input("Digite um numero inteiro: "))
soma = 0
while n != 0:
    resto = n % 10
    n = n // 10
    soma = soma + resto
print(soma)