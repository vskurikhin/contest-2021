#!/usr/bin/env python3

"""
Для строительства двумерной пирамиды используются прямоугольные блоки,
каждый из которых характеризуется шириной и высотой.
Можно поставить один блок на другой, только если ширина верхнего блока строго меньше ширины нижнего
(блоки нельзя поворачивать). Самым нижним в пирамиде может быть блок любой ширины.
По заданному набору блоков определите, пирамиду какой наибольшей высоты можно построить из них.

Формат ввода
В первой строке входных данных задается число N — количество блоков (1 ≤ N ≤ 100_000).
В следующих N строках задаются пары натуральных чисел wᵢ и hᵢ (1 ≤ wᵢ, hᵢ ≤ 10⁹) — ширина
и высота блока соответственно.

Формат вывода
Выведите одно целое число — максимальную высоту пирамиды.
"""

MAX_INT = 9223372036854775808


def read(name: str = 'input.txt') -> list[tuple[int, int]]:
    result = list[tuple[int, int]]()
    reader = open(name, 'r')
    n = int(reader.readline())
    for _ in range(n):
        a = [int(i) for i in reader.readline().split()]
        result.append((a[0], a[1]))
    reader.close()
    return result


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%d\n" % result)
    writer.close()
    pass


def solution(inp: list[tuple[int, int]]) -> int:
    m = dict[int, tuple[int, int]]()
    for _, t in enumerate(inp):
        w, _ = t
        if m.get(w):
            if m[w][1] < t[1]:
                m[w] = t
        else:
            m.setdefault(w, t)
    prev = MAX_INT
    result = 0
    for key in sorted(m.keys(), reverse=True):
        if key < prev:
            result += m[key][1]
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
