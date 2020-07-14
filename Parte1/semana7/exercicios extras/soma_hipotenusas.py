def é_hipotenusa(x):
    num = 1
    hipos = []
    divisor = 1
    divisores = 0
    while num <= x:
        while divisor <= x:
            div = num % divisor
            if div == 0:
                divisores +=1
            divisor += 1
        if divisores == 2:
            hipos.append(num)
        if num % 5 == 0 or num % 2 == 0:
            hipos.append(num)
        num += 1
        divisores = 0
    return hipos
x = int(input(" "))
print(é_hipotenusa(x))
