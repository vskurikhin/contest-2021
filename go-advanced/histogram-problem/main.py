#!/usr/bin/env python3

import unittest

"""
Разберём решение одной из самых популярных задач на стек. 
Пусть у нас есть гистограмма из nn столбцов, где i-ый столбец слева имеет высоту hᵢ.
Нужно вписать в гистограмму прямоугольник максимальной площади так, чтобы его точки не выходили
за границы столбцов.
"""


class Item:
    def __init__(self, index: int, value: int):
        self.index = index
        self.value = value

    def __str__(self) -> str:
        return "index: %d, value: %d" % (self.index, self.value)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: Item):
        self.items.append(item)

    def pop(self) -> Item:
        return self.items.pop()

    def peek(self) -> Item:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


def read(name: str = 'input_test1.txt') -> list[int]:
    reader = open(name, 'r')
    result = [int(n) for n in reader.readline().split(" ")]
    reader.close()
    return result


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%d" % result)
    writer.close()
    pass


def solution_on_histogram_problem(histogram: list[int]) -> int:
    if len(histogram) < 1:
        return 0

    stack_left = Stack()
    stack_right = Stack()

    left = []
    stack_left.push(Item(-1, 0))
    for idx in range(0, len(histogram)):
        while stack_left.size() > 1 and stack_left.peek().value > histogram[idx]:
            stack_left.pop()
        left.append(stack_left.peek().index)
        stack_left.push(Item(idx, histogram[idx]))

    right = [0] * len(histogram)
    stack_right.push(Item(len(histogram), 0))
    for idx in range(len(histogram) - 1, -1, -1):
        while stack_right.size() > 1 and stack_right.peek().value > histogram[idx]:
            stack_right.pop()
        right[idx] = stack_right.peek().index
        stack_right.push(Item(idx, histogram[idx]))

    max_square = 0
    for idx, value in enumerate(histogram):
        square = value * (right[idx] - left[idx] - 1)
        max_square = max(max_square, square)

    return max_square


def solution_on2_histogram_problem(histogram: list[int]) -> int:
    max_square = 0
    for idx, value in enumerate(histogram):
        square = value
        left = max(idx - 1, 0)
        while left > -1 and histogram[left] >= value:
            left -= 1
            square += value
        right = min(idx + 1, len(histogram) - 1)
        while right < len(histogram) and histogram[right] >= value:
            right += 1
            square += value
        max_square = max(max_square, square)

    return max_square


def histogram_problem() -> None:
    write(solution_on_histogram_problem(read()))
    pass


class TestHistogramProblem(unittest.TestCase):

    def test_main(self):
        main()

    def test_histogram_problem(self):
        histogram_problem()


def main():
    histogram_problem()
    pass


if __name__ == "__main__":
    main()
    pass
