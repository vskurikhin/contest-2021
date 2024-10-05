#!/usr/bin/env python3

"""
Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
Примечание. И даже эту задачу на Питоне можно решить в одну строчку.

Формат ввода
Вводятся два списка целых чисел. Все числа каждого списка находятся на отдельной строке.

Формат вывода

Выведите ответ на задачу.
"""


def read(name: str = 'input.txt') -> (list[int], list[int]):
    reader = open(name, 'r')
    list1 = [int(n) for n in reader.readline().split(" ")]
    list2 = [int(n) for n in reader.readline().split(" ")]
    reader.close()
    return list1, list2


def write(result: list[int], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    for e in result:
        writer.write("%d " % e)
    writer.close()
    pass


def solution(inp: tuple[list[int], list[int]]) -> list[int]:
    return sorted(set(inp[0]).intersection(set(inp[1])))


class Part3:
    class ProblemB:
        def __init__(self):
            write(solution(read()))


def main():
    Part3.ProblemB()
    pass


if __name__ == "__main__":
    main()
    pass
