#!/usr/bin/env python3

"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""
from typing import TextIO


def read_file(reader: TextIO) -> (list[int], dict[str, int]):
    a, m = list[int](), dict[str, int]()
    while True:
        line = reader.readline()
        if not line:
            break
        words = line.strip().split(r""" """)
        if words == ['']:
            continue
        for word in words:
            if word == '':
                continue
            i = m.setdefault(word, 0)
            a.append(i)
            m[word] = i + 1
    return a, m


def read(name: str = 'input.txt') -> (list[int], dict[str, int]):
    reader = open(name, 'r')
    a, m = read_file(reader)
    reader.close()
    return a, m


def write(result: list[int], name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    for i in result:
        writer.write("%d " % i)
    writer.write("\n")
    writer.close()
    pass


def solution(inp: tuple[list[int], dict[str, int]]) -> list[int]:
    return inp[0]


class Part4:
    class ProblemB:
        def __init__(self):
            write(solution(read()))


def main():
    Part4.ProblemB()
    pass


if __name__ == "__main__":
    main()
    pass
