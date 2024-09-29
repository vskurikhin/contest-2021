#!/usr/bin/env python3

"""
Выведите все элементы полученного дерева в порядке возрастания.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся нулем.
Сам ноль в последовательность не входит.
По данной последовательности требуется построить дерево.

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
        self.result = list[int]()

    def see(self, node: Node):
        self.result.append(node.data)


def traverse_inorder(node: Node, see: Callable[[Node], None]) -> None:
    if node is not None:
        traverse_inorder(node.left, see)
        see(node)
        traverse_inorder(node.right, see)


class Tree:
    def __init__(self):
        self.list = list[Node]()
        self.root = None

    def insert(self, value: int):
        self.root = insert(self.root, value)

    def traverse_inorder(self, see: Callable[[Node], None]) -> None:
        traverse_inorder(self.root, see)


def read(name: str = 'input.txt') -> Tree:
    reader = open(name, 'r')
    t = Tree()
    a = [int(i) for i in reader.readline().split()]
    for i in a:
        if i != 0:
            t.insert(i)
    reader.close()
    return t


def write(result: list[int], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    for _, v in enumerate(result):
        writer.write("%d\n" % v)
    writer.close()
    pass


def solution(inp: Tree) -> list[int]:
    o = Observer()
    inp.traverse_inorder(lambda n: o.see(n))
    return o.result


class Part8:
    class ProblemD:
        def __init__(self):
            write(solution(read()))


def main():
    Part8.ProblemD()
    pass


if __name__ == "__main__":
    main()
    pass
