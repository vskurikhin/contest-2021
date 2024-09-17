#!/usr/bin/env python3

"""
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор
и в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались,
сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
Для этого они занумеровали все цвета случайными числами.
На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
Номер любого цвета — это целое число в пределах от 0 до 10⁹.

Формат ввода
В первой строке входного файла записаны числа N и M — количество кубиков у Ани и Бори соответственно.
В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов кубиков Бори.

Формат вывода
Выведите сначала количество, а затем отсортированные по возрастанию номера цветов таких,
что кубики каждого цвета есть в обоих наборах, затем количество
и отсортированные по возрастанию номера остальных цветов у Ани,
потом количество и отсортированные по возрастанию номера остальных цветов у Бори.

"""
from typing import TextIO


def read(name: str = 'input.txt') -> (set[int], set[int]):
    reader = open(name, 'r')
    n, m = [int(n) for n in reader.readline().split(" ")]
    list1 = list[int]()
    for idx in range(n):
        list1.append(int(reader.readline()))
    list2 = list[int]()
    for idx in range(m):
        list2.append(int(reader.readline()))
    reader.close()
    return set(list1), set(list2)


def write_result(writer: TextIO, result: list[int]):
    writer.write("%d\n" % len(result))
    for e in result:
        writer.write("%d " % e)
    writer.write("\n")
    pass


def write(result1: list[int], result2: list[int], result3: list[int], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    write_result(writer, result1)
    write_result(writer, result2)
    write_result(writer, result3)
    writer.close()
    pass


# Average case: O(min(len(inp[0]), len(inp[1])))
# Worst Case: O(len(inp[0]) * len(inp[1]))
# notes: replace "min" with "max" if t is not a set
def solution1(inp: tuple[set[int], set[int]]) -> list[int]:
    return sorted(inp[0].intersection(inp[1]))


# Average case: O(len(inp[0]))
def solution2(inp: tuple[set[int], set[int]]) -> list[int]:
    return sorted(inp[0].difference(inp[1]))


# Average case: O(len(inp[0]))
def solution3(inp: tuple[set[int], set[int]]) -> list[int]:
    return sorted(inp[1].difference(inp[0]))


class Part3:
    class ProblemB:
        def __init__(self):
            inp = read()
            write(solution1(inp), solution2(inp), solution3(inp))


def main():
    Part3.ProblemB()
    pass


if __name__ == "__main__":
    main()
    pass
