#!/usr/bin/env python3

"""
Вася очень любит везде искать своё счастливое число K.
Каждый день он ходит в школу по улице, вдоль которой припарковано N машин.
Он заинтересовался вопросом, сколько существует наборов машин, стоящих подряд на местах с L до R,
что сумма их номеров равна K.
Помогите Васе узнать ответ на его вопрос.

Например, если число N=5, K=17, а номера машин равны 17, 7, 10, 7, 10, то существует 4 набора машин:

17 (L=1,R=1),
7, 10 (L=2,R=3),
10, 7 (L=3,R=4),
7, 10 (L=4,R=5)

Формат ввода
В первой строке входных данных задаются числа N и K (1 ≤ N ≤ 100_000, 1 ≤ K ≤ 10⁹).

Во второй строке содержится N чисел, задающих номера машин. Номера машин могут принимать значения от 1 до 999 включительно.

Формат вывода
Необходимо вывести одно число — количество наборов.
"""
from typing import Callable

MIN_INT = -9223372036854775808


def read(name: str = 'input.txt') -> (int, list[int]):
    reader = open(name, 'r')
    n, k = [int(i) for i in reader.readline().split()]
    a = [int(i) for i in reader.readline().split()]
    reader.close()
    return k, a


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%d\n" % result)
    writer.close()
    pass


def prefix_sum(inp: list[int]) -> list[int]:
    result = [1] * (len(inp) + 1)
    for i in range(1, len(inp) + 1):
        result[i] = result[i-1] + inp[i-1]
    return result


def right_binary_search(left: int, right: int, check: Callable[[int], bool]) -> int:
    if left > right:
        return MIN_INT
    while left < right:
        middle = (left + right + 1) // 2
        if check(middle):
            left = middle
        else:
            right = middle - 1
    if check(left):
        return left
    return MIN_INT


def solution(inp: tuple[int, list[int]]) -> int:
    r = 0
    k, a = inp
    pref_sum = prefix_sum(a)
    for i in range(len(pref_sum)):
        j = right_binary_search(i, len(pref_sum)-1, lambda x: (pref_sum[x] - pref_sum[i]) < k)
        if j == len(pref_sum) or j == MIN_INT:
            j = len(pref_sum) - 1
        r = sub_solution(pref_sum, i, j, k, r)
    return r


def sub_solution(pref_sum: list[int], i: int, j: int, k: int, r: int) -> int:
    for z in range(j, len(pref_sum)):
        s = pref_sum[z] - pref_sum[i]
        if s > k:
            return r
        if s == k:
            r += 1
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
