import primeiro_lex
def test_conta_letras():
    assert str(primeiro_lex.primeiro_lex(['AAAAAA', 'b'])) == str('AAAAAA')
def test_primeiro_lex1():
    assert str(primeiro_lex.primeiro_lex(['oĺá', 'A', 'a', 'casa'])) == str('A')
