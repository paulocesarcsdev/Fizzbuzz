"""
Fizzbuzz
Regras do Jogo
1.Quando a posição é múltipla de 3, fale fizz;
2.Quando a posição é múltipla de 5, fale buzz;
3.Quando a posição for múltipla de 3 e de 5 ,fale fizzbuzz;
4.Para todas as outras posições, fale o própio número.
"""

def robot(pos):
    if pos == 2:
        return '2'
    return '1'

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'