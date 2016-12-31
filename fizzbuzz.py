"""
Fizzbuzz
Regras do Jogo
1.Quando a posição é múltipla de 3, fale fizz;
2.Quando a posição é múltipla de 5, fale buzz;
3.Quando a posição for múltipla de 3 e de 5 ,fale fizzbuzz;
4.Para todas as outras posições, fale o própio número.
"""
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)

def robot(pos):
    say = str(pos)


    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
       say = 'fizz'
    return say


def assert_equal(result, expected, line):
    msg = 'Fail: Line {} got {} expecting {}'

    if not result == expected:
        print(msg.format(line, result, expected))

if __name__ == '__main__':
    assert_equal(robot(1),  '1', '35')
    assert_equal(robot(2),  '2', '36')
    assert_equal(robot(4),  '4', '37')
    assert_equal(robot(3),  'fizz', '38')
    assert_equal(robot(6),  'fizz', '39')
    assert_equal(robot(9),  'fizz', '40')
    assert_equal(robot(5),  'buzz', '41')
    assert_equal(robot(10),  'buzz', '42')
    assert_equal(robot(20),  'buzz', '43')
    assert_equal(robot(15),  'fizzbuzz', '44')
    assert_equal(robot(30),  'fizzbuzz', '45')
