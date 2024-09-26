#!/usr/bin/env python3

"""
Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.

Формат ввода
В первой строке входных данных содержатся числа N и K (1 ≤ N, K ≤ 100_001).
Во второй строке задаются N чисел первого массива, отсортированного по неубыванию,
а в третьей строке – K чисел второго массива.
Каждое число в обоих массивах по модулю не превосходит 2⋅10⁹.

Формат вывода
Для каждого из K чисел выведите в отдельную строку число из первого массива,
наиболее близкое к данному.
Если таких несколько, выведите меньшее из них.
"""
from typing import Callable

MIN_INT = -2**64//2


def read(name: str = 'input.txt') -> (list[int], list[int]):
    reader = open(name, 'r')
    _, _ = [int(i) for i in reader.readline().split()]
    a = [int(i) for i in reader.readline().split()]
    b = [int(i) for i in reader.readline().split()]
    reader.close()
    return a, b


def write(result: list[int], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    for i in range(len(result)):
        writer.write("%d\n" % result[i])
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


def solution(inp: tuple[list[int], list[int]]) -> list[int]:
    a, b = inp
    r = [0] * len(b)
    for i, v in enumerate(b):
        j = left_binary_search(0, len(a) - 1, lambda x: a[x] >= v)
        if j == MIN_INT:
            r[i] = a[len(a) - 1]
        elif a[j] == v:
            r[i] = v
        elif j != 0 and abs(a[j-1]-v) <= abs(a[j]-v):
            r[i] = a[j-1]
        else:
            r[i] = a[j]
    return r


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
