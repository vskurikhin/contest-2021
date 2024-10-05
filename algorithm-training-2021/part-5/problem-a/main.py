#!/usr/bin/env python3

"""
Глеб обожает шоппинг. Как-то раз он загорелся идеей подобрать себе майку и штаны так,
чтобы выглядеть в них максимально стильно. В понимании Глеба стильность одежды тем больше,
чем меньше разница в цвете элементов его одежды.

В наличии имеется N (1 ≤ N ≤ 100_000) маек и M (1 ≤ M ≤ 100_000) штанов,
про каждый элемент известен его цвет (целое число от 1 до 10_000_000).
Помогите Глебу выбрать одну майку и одни штаны так, чтобы разница в их цвете была как можно меньше.

Формат ввода
Сначала вводится информация о майках: в первой строке целое число N (1 ≤ N ≤ 100_000)
и во второй N целых чисел от 1 до 10_000_000 — цвета имеющихся в наличии маек.
Гарантируется, что номера цветов идут в возрастающем порядке (в частности, цвета никаких двух маек не совпадают).

Далее в том же формате идёт описание штанов: их количество M (1 ≤ M ≤ 100_000)
и в следующей строке M целых чисел от 1 до 10_000_000 в возрастающем порядке — цвета штанов.

Формат вывода
Выведите пару неотрицательных чисел — цвет майки и цвет штанов, которые следует выбрать Глебу.
Если вариантов выбора несколько, выведите любой из них.
"""
from typing import Callable

MAX_INT = 9223372036854775808
MIN_INT = -9223372036854775808


def read(name: str = 'input.txt') -> (list[int], list[int]):
    reader = open(name, 'r')
    _ = int(reader.readline())
    a = [int(i) for i in reader.readline().split()]
    _ = int(reader.readline())
    b = [int(i) for i in reader.readline().split()]
    reader.close()
    return a, b


def write(result: tuple[int, int], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%d %d\n" % (result[0], result[1]))
    writer.close()
    pass


def left_binary_search(left: int, right: int, check: Callable[[int], bool]) -> int:
    if left > right:
        return MIN_INT
    while left < right:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle + 1
    if check(left):
        return left
    return MIN_INT


def solution(inp: tuple[list[int], list[int]]) -> (int, int):
    result = tuple((0, 0))
    h, m = inp
    min_diff = MAX_INT
    for i, v in enumerate(h):
        j = left_binary_search(0, len(m)-1, lambda k: m[k] >= v)
        if j == MIN_INT:
            j = len(m) - 1
        if j > 0:
            if min_diff > abs(v - m[j-1]):
                min_diff = abs(v - m[j-1])
                result = v, m[j-1]
        if min_diff > abs(v - m[j]):
            min_diff = abs(v - m[j])
            result = v, m[j]
    return result


class Part4:
    class ProblemD:
        def __init__(self):
            write(solution(read()))


def main():
    Part4.ProblemD()
    pass


if __name__ == "__main__":
    main()
    pass
