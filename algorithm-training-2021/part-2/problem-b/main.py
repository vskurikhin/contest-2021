#!/usr/bin/env python3

import sys

ASCENDING = "ASCENDING"
CONSTANT = "CONSTANT"
DESCENDING = "DESCENDING"
RANDOM = "RANDOM"
WEAKLY_ASCENDING = "WEAKLY ASCENDING"
WEAKLY_DESCENDING = "WEAKLY DESCENDING"

"""
Дан список. Определите, является ли он монотонно возрастающим
(то есть верно ли, что каждый элемент этого списка больше предыдущего).

Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""


def part_2_problem_b(name: str = 'input.txt') -> str:
    reader = open(name, 'r')
    result = ""
    previous = None
    while True:
        current = int(reader.readline())
        if current == -2000000000:
            break
        else:
            if previous and type(previous) is int:
                result = part_2_solution_b(previous, current, result)
            previous = current
    if result == "":
        result = "RANDOM"
    reader.close()
    return result


def write(result: str, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write(result)
    writer.close()
    pass


def part_2_solution_b_ascending(previous: int, current: int) -> str:
    if previous < current:
        return ASCENDING
    if previous == current:
        return WEAKLY_ASCENDING
    else:
        return RANDOM


def part_2_solution_b_constant(previous: int, current: int) -> str:
    if previous == current:
        return CONSTANT
    if previous < current:
        return WEAKLY_ASCENDING
    if previous > current:
        return WEAKLY_DESCENDING


def part_2_solution_b_descending(previous: int, current: int) -> str:
    if previous > current:
        return DESCENDING
    if previous == current:
        return WEAKLY_DESCENDING
    else:
        return RANDOM


def part_2_solution_b_empty(previous: int, current: int) -> str:
    if previous == current:
        return CONSTANT
    if previous < current:
        return ASCENDING
    if previous > current:
        return DESCENDING


def part_2_solution_b_weakly_ascending(previous: int, current: int) -> str:
    if previous < current or previous == current:
        return WEAKLY_ASCENDING
    else:
        return RANDOM


def part_2_solution_b_weakly_descending(previous: int, current: int) -> str:
    if previous > current or previous == current:
        return WEAKLY_DESCENDING
    else:
        return RANDOM


def part_2_solution_b(previous: int, current: int, result: str) -> str:
    if result == "":
        return part_2_solution_b_empty(previous, current)
    if result == CONSTANT:
        return part_2_solution_b_constant(previous, current)
    if result == ASCENDING:
        return part_2_solution_b_ascending(previous, current)
    if result == WEAKLY_ASCENDING:
        return part_2_solution_b_weakly_ascending(previous, current)
    if result == DESCENDING:
        return part_2_solution_b_descending(previous, current)
    if result == WEAKLY_DESCENDING:
        return part_2_solution_b_weakly_descending(previous, current)
    return result


def main():
    write(part_2_problem_b())
    pass


if __name__ == "__main__":
    main()
    pass
