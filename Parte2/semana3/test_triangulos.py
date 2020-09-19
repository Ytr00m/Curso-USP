import Questoes
import pytest
class TestTriangulo:
    @pytest.mark.parametrize("ladoA, ladoB, ladoC, tipo_lado_esperado", [
        (1, 2, 3, 'escaleno'),
        (3, 3, 3, 'equilátero'),
        (22, 22, 33, 'isósceles'),
        (22, 23, 22, 'isósceles')
        ])
    def test_tri(self, ladoA, ladoB, ladoC, tipo_lado_esperado):
        t = Questoes.Triangulo(ladoA, ladoB, ladoC)
        assert t.tipo_lado() == tipo_lado_esperado

    @pytest.mark.parametrize("ladoA1, ladoB1, ladoC1, ladoA2, ladoB2, ladoC2, semelhante", [
        (3, 5, 4, 9, 15, 12, True),
        (6, 8, 10, 30, 40, 50, True),
        (5, 12, 13, 10, 24, 26, True),
        (5, 5, 3, 2, 5, 7, False),
        (7, 8, 9, 7, 10, 16, False),
        (3, 3, 3, 5, 5, 5, True)
        ])
    def test_retangulo(self, ladoA1, ladoB1, ladoC1, ladoA2, ladoB2, ladoC2, semelhante):
        t1 = Questoes.Triangulo(ladoA1, ladoB1, ladoC1)
        t2 = Questoes.Triangulo(ladoA2, ladoB2, ladoC2)
        assert t1.semelhantes(t2) == semelhante
    
    @pytest.mark.parametrize("ladoA, ladoB, ladoC, retangulo", [
        (3, 5, 4, True),
        (6, 8, 10, True),
        (5, 12, 13, True),
        (5, 5, 3, False),
        (7, 8, 9, False),
        (3, 3, 3, False)
        ])
    def test_retangulo(self, ladoA, ladoB, ladoC, retangulo):
        t = Questoes.Triangulo(ladoA, ladoB, ladoC)
        assert t.retangulo() == retangulo


