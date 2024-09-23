#!/usr/bin/env python3

"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""
from collections import OrderedDict
from typing import TextIO

MIN_INT = -9223372036854775808

def read_file(reader: TextIO) -> dict[str, int]:
    m = dict[str, int]()
    while True:
        line = reader.readline()
        if not line:
            break
        words = line.strip().split(r""" """)
        for word in words:
            if word == '':
                continue
            m[word] = m.setdefault(word, 0) + 1
    return m


def read(name: str = 'input.txt') -> dict[str, int]:
    reader = open(name, 'r')
    m = read_file(reader)
    reader.close()
    return m


def write(result: str, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%s\n" % result)
    writer.close()
    pass


def solution(inp: dict[str, int]) -> str:
    max_result = tuple[str, int](("", MIN_INT))
    for word in sorted(inp.keys()):
        if inp[word] > max_result[1]:
            max_result = (word, inp[word])
    return max_result[0]


class Part4:
    class ProblemC:
        def __init__(self):
            write(solution(read()))


def main():
    Part4.ProblemC()
    pass


if __name__ == "__main__":
    main()
    pass
