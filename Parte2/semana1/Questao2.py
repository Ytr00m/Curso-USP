def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        somaDasMatrizes = []
        countLinha = 0
        for i in range(len(m1)):
            linhas = []
            countColuna = 0
            for j in range(len(m1[0])):
                linhas.append(m1[countLinha][countColuna] + m2[countLinha][countColuna])
                countColuna += 1
            countLinha += 1
            somaDasMatrizes.append(linhas)
        return somaDasMatrizes
    
    else:
        return False