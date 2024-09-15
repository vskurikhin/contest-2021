#!/usr/bin/env python3

from typing import Callable

"""
Дан массив из N целых чисел. Все числа от −10⁹ до 10⁹.

Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от L до R?”.

Формат ввода
Число N (1 ≤ N ≤ 10⁵). Далее N целых чисел.

Затем число запросов K (1 ≤ K ≤ 10⁵).

Далее K пар чисел L, R (−10⁹ ≤ L ≤ R ≤ 10⁹) — собственно запросы.

Формат вывода
Выведите K чисел — ответы на запросы. 
"""


def read(name: str = 'input.txt') -> (list[int], list[tuple[int, int]]):
    reader = open(name, 'r')
    _ = int(reader.readline())
    result = [int(n) for n in reader.readline().split(" ")]
    k = int(reader.readline())
    request = []
    for _ in range(k):
        l, r = [int(n) for n in reader.readline().split(" ")]
        request.append((l, r))
    reader.close()
    return result, request


def l_bin_search(left: int, right: int, check: Callable[[int], bool]) -> int:
    if left > right:
        return -1
    while left < right:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle + 1
    return left


def r_bin_search(left: int, right: int, check: Callable[[int], bool]) -> int:
    if left > right:
        return -1
    while left < right:
        middle = (left + right + 1) // 2
        if check(middle):
            left = middle
        else:
            right = middle - 1
    return left


def part_2_problem_c(inp: list[int], request: list[tuple[int, int]]) -> list[int]:
    result = []
    inp.sort()
    for idx, tup in enumerate(request):
        left_idx = l_bin_search(0, len(inp), lambda i: inp[i] >= tup[0])
        right_idx = r_bin_search(0, len(inp) - 1, lambda i: inp[i] <= tup[1])
        result.append(right_idx - left_idx + 1)
    return result


def write(result: list[int], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    for idx in range(len(result)):
        writer.write("%d " % result[idx])
    writer.close()
    pass


def main():
    inp, request = read()
    write(part_2_problem_c(inp, request))
    pass


if __name__ == "__main__":
    main()
    pass
