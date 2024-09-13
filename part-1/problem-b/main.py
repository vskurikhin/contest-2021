#!/usr/bin/env python3

import unittest

"""
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами. Если это возможно, выведите строку YES, иначе выведите строку NO.

Треугольник — это три точки, не лежащие на одной прямой.
Формат ввода

Вводятся три натуральных числа.
Формат вывода

Выведите ответ на задачу. 
"""


class TestProblemsB(unittest.TestCase):

    def test_main(self):
        main()

    def test_problems_a(self):
        problem_b()


def read(name: str = 'input.txt') -> (int, int, int):
    reader = open(name, 'r')
    a = int(reader.readline())
    b = int(reader.readline())
    c = int(reader.readline())
    reader.close()
    return a, b, c


def write(result: str, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%s" % result)
    writer.close()
    pass


def sub(a: int, b: int, c: int) -> int:
    return a - b - c


def solution_b(a: int, b: int, c: int) -> bool:
    m = max(a, b)
    m = max(m, c)
    if m == a:
        if sub(a, b, c) < 0:
            return True
        else:
            return False
    if m == b:
        if sub(b, a, c) < 0:
            return True
        else:
            return False
    if m == c:
        if sub(c, a, b) < 0:
            return True
        else:
            return False
    return False


def problem_b() -> None:
    a, b, c = read()
    if solution_b(a, b, c):
        write("YES")
    else:
        write("NO")
    pass


def main():
    problem_b()
    pass


if __name__ == "__main__":
    main()
    pass
