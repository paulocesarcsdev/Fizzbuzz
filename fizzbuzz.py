"""
Fizzbuzz
Regras do Jogo
1.Quando a posição é múltipla de 3, fale fizz;
2.Quando a posição é múltipla de 5, fale buzz;
3.Quando a posição for múltipla de 3 e de 5 ,fale fizzbuzz;
4.Para todas as outras posições, fale o própio número.
"""

def multiple_of_3(num):
    return num % 3 == 0

def robot(pos):
    say = str(pos)
    if pos % 3 == 0 and pos % 5 == 0:
        say = 'fizzbuzz'

    elif pos % 5 == 0:
        say = 'buzz'

    elif multiple_of_3(pos):
       say = 'fizz'

    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'