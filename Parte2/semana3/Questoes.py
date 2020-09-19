class Triangulo:
    def __init__(self, ladoa, ladob, ladoc):
        self.a = ladoa
        self.b = ladob
        self.c = ladoc

    def perimetro(self): #Questao 1

        return self.a + self.b + self.c

    def tipo_lado(self): #Questao 2
        a, b, c = str(self.a), str(self.b), str(self.c)
        lista = a + b + c
        ladosIguaisA = lista.count(a)
        ladosIguaisB = lista.count(b)
        ladosIguaisC = lista.count(c)
        
        if ladosIguaisA == 3 and ladosIguaisB == 3 and ladosIguaisC == 3:
            return 'equilátero'

        elif ladosIguaisA == 2 or ladosIguaisB == 2 or ladosIguaisC == 2:
            return 'isósceles'

        else:
            return 'escaleno'

    def retangulo(self): #Exercicios extras: Triangulo Retangulo
        A, B, C = self.a ** 2, self.b ** 2, self.c ** 2
        a, b, c = str(A), str(B), str(C)
        lista = a + b + c
        
        if lista.count(str(A + B)) == 1 or lista.count(str(A + C)) == 1 or lista.count(str(C + B)) == 1:
            return True

        else: 
            return False

    def semelhantes(self, triangulo): #Exercicios extras: Triangulos Semelhantes
        lista1, lista2, lista3 = [self.a, self.b, self.c], [triangulo.a, triangulo.b, triangulo.c], []
        count = 0

        for i in lista1:
            lista3.append(i / lista2[count])
            count += 1

        ladosSemelhantes = lista3.count(lista1[0] / lista2[0])
        if ladosSemelhantes == 3:
            return True

        else: 
            return False
        