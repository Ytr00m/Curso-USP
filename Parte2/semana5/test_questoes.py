import pytest
import Questao1
import Questao2
import Extras.insertion_sort as insertion

class Testquest:
    @pytest.mark.parametrize("lista, elemento, resultado", [

        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, 7),
        ([100, 192, 7823, 699999], 7823, 2),
        ([1, 2, 3, 5], 5, 3)

    ])
    def test_Questao1(self, lista, elemento,resultado):

        assert Questao1.busca(lista, elemento) == resultado

    @pytest.mark.parametrize("lista, resultado", [

        ([7, 9, 2, 4, 0.352, 3123, 43, -13294], [-13294, 0.352, 2, 4, 7, 9, 43, 3123]),
        ([10, 7, 9, 4, 6, 3, 1, 2, 8, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([2, 6, 4, 8, 12, 20, 16, 0], [0, 2, 4, 6, 8, 12, 16, 20])

    ])
    def test_Questao2(self, lista, resultado):
        
        assert Questao2.bubble_sort(lista) == resultado

    @pytest.mark.parametrize("lista, resultado", [

        ([7, 9, 2, 4, 0.352, 3123, 43, -13294], [-13294, 0.352, 2, 4, 7, 9, 43, 3123]),
        ([10, 7, 9, 4, 6, 3, 1, 2, 8, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([2, 6, 4, 8, 12, 20, 16, 0], [0, 2, 4, 6, 8, 12, 16, 20])

    ])
    def test_insertion_sort(self, lista, resultado):
        
        assert insertion.insertion_sort(lista) == resultado
