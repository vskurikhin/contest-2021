#!/usr/bin/env python3

"""
Реализуйте бинарное дерево поиска для целых чисел.
Программа получает на вход последовательность целых чисел и строит из них дерево.
Элементы в деревья добавляются в соответствии с результатом поиска их места.
Если элемент уже существует в дереве, добавлять его не надо.
Балансировка дерева не производится.

Формат ввода
На вход программа получает последовательность натуральных чисел.
Последовательность завершается числом 0, которое означает конец ввода, и добавлять его в дерево не надо.

Формат вывода
Выведите единственное число – высоту получившегося дерева.
"""
from typing import Callable

MIN_INT = -2 ** 64 // 2


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


def max_height(left: Node, right: Node) -> int:
    if isinstance(left, Node) and isinstance(right, Node):
        return max(left.height + 1, right.height + 1)
    elif isinstance(left, Node):
        return left.height + 1
    elif isinstance(right, Node):
        return right.height + 1
    else:
        return 1


def insert(node: Node, value: int) -> Node:
    if node is None:
        node = Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    node.height = max_height(node.left, node.right)
    return node


def traverse_inorder(node: Node, see: Callable[[Node], None]) -> None:
    if node is not None:
        traverse_inorder(node.left, see)
        see(node)
        traverse_inorder(node.right, see)


def traverse_preorder(node: Node, see: Callable[[Node], None]) -> None:
    if node is not None:
        see(node)
        traverse_preorder(node.left, see)
        traverse_preorder(node.right, see)


def traverse_postorder(node: Node, see: Callable[[Node], None]) -> None:
    if node is not None:
        traverse_preorder(node.left, see)
        traverse_preorder(node.right, see)
        see(node)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        self.root = insert(self.root, value)

    def traverse_inorder(self, see: Callable[[Node], None] = lambda x: print(x)) -> None:
        traverse_inorder(self.root, see)

    def traverse_preorder(self, see: Callable[[Node], None] = lambda x: print(x)) -> None:
        traverse_preorder(self.root, see)

    def traverse_postorder(self, see: Callable[[Node], None] = lambda x: print(x)) -> None:
        traverse_postorder(self.root, see)


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
    return inp.root.height if isinstance(inp.root, Node) else MIN_INT


class Part8:
    class ProblemA:
        def __init__(self):
            write(solution(read()))


def main():
    Part8.ProblemA()
    pass


if __name__ == "__main__":
    main()
    pass
