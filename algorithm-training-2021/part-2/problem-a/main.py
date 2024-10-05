#!/usr/bin/env python3

import sys

"""
Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).

Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""


def read(name: str = 'input.txt') -> list[int]:
    reader = open(name, 'r')
    result = [int(n) for n in reader.readline().split(" ")]
    reader.close()
    return result


def write(result: bool, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    if result:
        writer.write("YES")
    else:
        writer.write("NO")
    writer.close()
    pass


def part_2_solution_a(inp: list[int]) -> bool:
    for idx, value in enumerate(inp):
        if idx > 0:
            if value <= inp[idx-1]:
                return False
    return True


def part_2_problem_a() -> None:
    write(part_2_solution_a(read()))
    pass


def main():
    part_2_problem_a()
    pass


if __name__ == "__main__":
    main()
    pass
