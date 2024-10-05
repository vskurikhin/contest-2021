#!/usr/bin/env python3

"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу.
Формат ввода

В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.
Формат вывода

Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них. 
"""


def read(name: str = 'input.txt') -> (list[int], int):
    reader = open(name, 'r')
    _ = int(reader.readline())
    result = [int(n) for n in reader.readline().split(" ")]
    x = int(reader.readline())
    reader.close()
    return result, x


def part_2_problem_c(inp: list[int], x: int) -> int:
    min_index = -1
    min_value = +1001
    for idx, value in enumerate(inp):
        difference = abs(value - x)
        if difference < min_value:
            min_index = idx
            min_value = difference
    return inp[min_index]


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write(str(result))
    writer.close()
    pass


def main():
    inp, x = read()
    write(part_2_problem_c(inp, x))
    pass


if __name__ == "__main__":
    main()
    pass
