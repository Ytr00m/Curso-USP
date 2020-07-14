def maior_primo(k):
    divisor = 2
    num = 1
    cont = 1
    ehprimo = None
    while cont < k:
        primo = divisor % num
        num = num + 1
        cont = cont + 1
        divisor += 1
        if primo != 0 and (num % 2) != 0:
            ehprimo = num
            if k % 2 == 0 and k % 3 == 1:
                ehprimo -= 2
    return ehprimo
