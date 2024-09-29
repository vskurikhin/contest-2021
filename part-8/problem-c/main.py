#!/usr/bin/env python3

"""
Выведите второй по величине элемент в построенном дереве. Гарантируется, что такой найдется.

Формат ввода
Дана последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит.

Формат вывода
Выведите ответ на задачу.
"""
from typing import Callable

MIN_INT = -2 ** 64 // 2


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        left_data = self.left.data if isinstance(self.left, Node) else 0
        right_data = self.right.data if isinstance(self.right, Node) else 0
        return "value: %d, left: %d, right: %d" % (self.data, left_data, right_data)


def insert(node: Node, value: int) -> Node:
    if node is None:
        node = Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node


class Observer:
    def __init__(self):
        self.idx = 0
        self.result = MIN_INT


def traverse_reverse_order(node: Node, see: Observer) -> None:
    if node is not None:
        traverse_reverse_order(node.right, see)
        if see.idx == 2:
            return
        if see.idx == 1:
            see.result = node.data
        see.idx += 1
        traverse_reverse_order(node.left, see)


class Tree:
    def __init__(self):
        self.list = list[Node]()
        self.root = None

    def insert(self, value: int):
        self.root = insert(self.root, value)

    def traverse_reverse_order(self, see: Observer) -> None:
        traverse_reverse_order(self.root, see)


def read(name: str = 'input.txt') -> Tree:
    reader = open(name, 'r')
    t = Tree()
    a = [int(i) for i in reader.readline().split()]
    for i in a:
        if i != 0:
            t.insert(i)
    reader.close()
    return t


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%d\n" % result)
    writer.close()
    pass


def solution(inp: Tree) -> int:
    see = Observer()
    inp.traverse_reverse_order(see)
    return see.result


class Part8:
    class ProblemC:
        def __init__(self):
            write(solution(read()))


def main():
    Part8.ProblemC()
    pass


if __name__ == "__main__":
    main()
    pass
