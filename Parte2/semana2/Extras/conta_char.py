def conta_letras(frase, contar='vogais'):
    count = 0
    if contar == 'vogais':
        for i in frase:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                count += 1
        return count
    if contar == 'consoantes':
        for i in frase:
            if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U' and i != ' ':
                count += 1
        return count
