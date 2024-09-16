#!/usr/bin/env python3

"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей
и выведите количество таких элементов.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
Формат вывода

Выведите ответ на задачу.
"""


def read(name: str = 'input.txt') -> list[int]:
    reader = open(name, 'r')
    result = [int(n) for n in reader.readline().split(" ")]
    reader.close()
    return result


def part_2_problem_d(inp: list[int]) -> int:
    result = 0
    for idx, value in enumerate(inp):
        if idx == 0 or idx == (len(inp) - 1):
            continue
        if inp[idx - 1] < value and value > inp[idx + 1]:
            result += 1
    return result


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write(str(result))
    writer.close()
    pass


def main():
    write(part_2_problem_d(read()))
    pass


if __name__ == "__main__":
    main()
    pass
