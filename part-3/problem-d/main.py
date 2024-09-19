#!/usr/bin/env python3

"""
Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""
from typing import TextIO


def read(name: str = 'input.txt') -> set[str]:
    result = set[str]()
    reader = open(name, 'r')
    for line in reader.readlines():
        result = result.union([str(n) for n in line.split()])
    reader.close()
    return result


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write(str(result))
    writer.close()
    pass


def solution(inp: set[str]) -> int:
    return len(inp)


class Part3:
    class ProblemD:
        def __init__(self):
            write(solution(read()))


def main():
    Part3.ProblemD()
    pass


if __name__ == "__main__":
    main()
    pass
