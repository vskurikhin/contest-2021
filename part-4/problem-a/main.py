#!/usr/bin/env python3

"""
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны. Для одного данного слова определите его синоним.

Формат ввода
Программа получает на вход количество пар синонимов N.
Далее следует N строк, каждая строка содержит ровно два слова-синонима.
После этого следует одно слово.

Формат вывода
Программа должна вывести синоним к данному слову.

Примечание
Эту задачу можно решить и без словарей (сохранив все входные данные в списке),
но решение со словарем будет более простым.
"""


def read(name: str = 'input.txt') -> (dict[str, str], str):
    result = dict[str, str]()
    reader = open(name, 'r')
    n = int(reader.readline().strip())
    for _ in range(n):
        word1, word2 = [str(n) for n in reader.readline().split()]
        result[word1], result[word2] = word2, word1
    word = reader.readline().strip()
    reader.close()
    return result, word


def write(result: str, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write(result)
    writer.close()
    pass


def solution(inp: tuple[dict[str, str], str]) -> str:
    return inp[0][inp[1]]


class Part4:
    class ProblemA:
        def __init__(self):
            write(solution(read()))


def main():
    Part4.ProblemA()
    pass


if __name__ == "__main__":
    main()
    pass
