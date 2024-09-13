#!/usr/bin/env python3

import unittest


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0


def is_empty(self):
    return self.size == 0


def push(self, x):
    if self.size != self.max_n:
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1


def pop(self):
    if self.is_empty():
        return None
    x = self.queue[self.head]
    self.queue[self.head] = None
    self.head = (self.head + 1) % self.max_n
    self.size -= 1
    return x


class TestStringMethods(unittest.TestCase):

    def test_main(self):
        main()


def main():
    pass


if __name__ == "__main__":
    main()
    pass
