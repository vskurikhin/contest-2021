#!/usr/bin/env python3

import sys
import unittest

"""
В офисе, где работает программист Петр, установили кондиционер нового типа. Этот кондиционер отличается особой простотой в управлении. У кондиционера есть всего лишь два управляемых параметра: желаемая температура и режим работы.

Кондиционер может работать в следующих четырех режимах:

«freeze» — охлаждение. В этом режиме кондиционер может только уменьшать температуру. Если температура в комнате и так не больше желаемой, то он выключается.

«heat» — нагрев. В этом режиме кондиционер может только увеличивать температуру. Если температура в комнате и так не меньше желаемой, то он выключается.

«auto» — автоматический режим. В этом режиме кондиционер может как увеличивать, так и уменьшать температуру в комнате до желаемой.

«fan» — вентиляция. В этом режиме кондиционер осуществляет только вентиляцию воздуха и не изменяет температуру в комнате.

Кондиционер достаточно мощный, поэтому при настройке на правильный режим работы он за час доводит температуру в комнате до желаемой.

Требуется написать программу, которая по заданной температуре в комнате troom, установленным на кондиционере желаемой температуре tcond и режиму работы определяет температуру, которая установится в комнате через час.
Формат ввода

Первая строка входного файла содержит два целых числа troom, и tcond, разделенных ровно одним пробелом (–50 ≤ troom ≤ 50, –50 ≤ tcond ≤ 50).

Вторая строка содержит одно слово, записанное строчными буквами латинского алфавита — режим работы кондиционера.
Формат вывода

Выходной файл должен содержать одно целое число — температуру, которая установится в комнате через час.
"""


class TestMethods(unittest.TestCase):

    def test_main(self):
        main()

    def test_problems_a(self):
        problem_a()


def read(name: str = 'input.txt') -> (int, int, str):
    reader = open(name, 'r')
    room, cond = [int(n) for n in reader.readline().split(" ")]
    word = reader.readline().strip()
    reader.close()
    return room, cond, word


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%d" % result)
    writer.close()
    pass


def freeze(room: int, cond: int) -> int:
    if room < cond:
        return room
    return cond


def heat(room: int, cond: int) -> int:
    if room > cond:
        return room
    return cond


def auto(_: int, cond: int) -> int:
    return cond


def fan(room: int, _: int) -> int:
    return room


def solution_a(room: int, cond: int, word: str) -> int:
    if word == "freeze":
        return freeze(room, cond)
    if word == "heat":
        return heat(room, cond)
    if word == "auto":
        return auto(room, cond)
    if word == "fan":
        return fan(room, cond)
    return 0


def problem_a() -> None:
    room, cond, word = read()
    write(solution_a(room, cond, word))
    pass


def main():
    problem_a()
    pass


if __name__ == "__main__":
    main()
    pass
