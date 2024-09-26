#!/usr/bin/env python3

"""
В бинарное дерево поиска добавляются элементы.
Выведите глубину для каждого добавленного элемента в том порядке, как они добавлялись.
Если элемент уже есть в дереве, то ничего добавлять и выводить не нужно.
Глубиной называется расстояние от корня дерева до элемента включительно.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит. По данной последовательности требуется построить дерево.

Формат вывода
Выведите ответ на задачу.
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self) -> str:
        left_data = self.left.data if isinstance(self.left, Node) else 0
        right_data = self.right.data if isinstance(self.right, Node) else 0
        return "value: %d, height: %d, left: %d, right: %d" % (self.data, self.height, left_data, right_data)


def insert(node: Node, value: int, a: list[Node], h: int) -> Node:
    if node is None:
        node = Node(value)
        node.height = h + 1
        a.append(node)
    if value < node.data:
        node.left = insert(node.left, value, a, h + 1)
    elif value > node.data:
        node.right = insert(node.right, value, a, h + 1)
    return node


class Tree:
    def __init__(self):
        self.list = list[Node]()
        self.root = None

    def insert(self, value: int):
        self.root = insert(self.root, value, self.list, 0)


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
    for i in range(len(result)):
        writer.write("%d " % result[i])
    writer.write("\n")
    writer.close()
    pass


def solution(inp: Tree) -> list[int]:
    return [node.height for node in inp.list]


class Part8:
    class ProblemB:
        def __init__(self):
            write(solution(read()))


def main():
    Part8.ProblemB()
    pass


if __name__ == "__main__":
    main()
    pass
