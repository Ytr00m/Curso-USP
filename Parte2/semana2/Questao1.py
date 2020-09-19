def maiusculas(frase):
    letras_maiusculas = ""
    for i in frase:
        if ord(i) >= 65 and ord(i) <= 90:
            letras_maiusculas += i
    return letras_maiusculas

