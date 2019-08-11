def n_primos(x):
    divisor = 1
    divisores = 0
    primos = 0
    num = 1
    while num <= x:
        while divisor <= num:
            div = num % divisor
            if div == 0:
                divisores +=1
            divisor += 1
        if divisores == 2:
            primos += 1
        num += 1
        divisores = 0
        divisor = 1
    return primos
    
