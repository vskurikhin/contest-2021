#!/usr/bin/env python3

"""
Реализуйте двоичный поиск в массиве

Формат ввода
В первой строке входных данных содержатся натуральные числа N и K (1 ≤ N, K ≤ 100_000).
Во второй строке задаются N элементов первого массива, а в третьей строке – K элементов второго массива.
Элементы обоих массивов - целые числа, каждое из которых по модулю не превосходит 10⁹

Формат вывода
Требуется для каждого из K чисел вывести в отдельную строку "YES",
если это число встречается в первом массиве, и "NO" в противном случае.
"""

MIN_INT = -2**64//2


def read(name: str = 'input.txt') -> (list[int], list[int]):
    reader = open(name, 'r')
    _, _ = [int(i) for i in reader.readline().split()]
    a = [int(i) for i in reader.readline().split()]
    b = [int(i) for i in reader.readline().split()]
    reader.close()
    return a, b


def write(result: list[bool], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    for i in range(len(result)):
        if result[i]:
            writer.write("YES\n")
        else:
            writer.write("NO\n")
    writer.close()
    pass


def binary_search(arr, x, left: int, right: int) -> int:
    if right <= left:  # промежуток пуст
        return MIN_INT
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального значит следует искать в левой половине
        return binary_search(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binary_search(arr, x, mid + 1, right)


def solution(inp: tuple[list[int], list[int]]) -> list[bool]:
    a, b = inp
    r = [False] * len(b)
    for i, v in enumerate(b):
        if binary_search(a, v, 0, len(a)) != MIN_INT:
            r[i] = True
    return r


class Part6:
    class ProblemA:
        def __init__(self):
            write(solution(read()))


def main():
    Part6.ProblemA()
    pass


if __name__ == "__main__":
    main()
    pass
