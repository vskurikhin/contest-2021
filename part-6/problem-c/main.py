#!/usr/bin/env python3

"""
Когда Петя учился в школе, он часто участвовал в олимпиадах по информатике, математике и физике.
Так как он был достаточно способным мальчиком и усердно учился, то на многих из этих олимпиад он получал дипломы.
К окончанию школы у него накопилось n дипломов, причём, как оказалось, все они имели одинаковые размеры:
w — в ширину и h — в высоту.
Сейчас Петя учится в одном из лучших российских университетов и живёт в общежитии со своими одногруппниками.
Он решил украсить свою комнату, повесив на одну из стен свои дипломы за школьные олимпиады.
Так как к бетонной стене прикрепить дипломы достаточно трудно,
то он решил купить специальную доску из пробкового дерева,
чтобы прикрепить её к стене, а к ней — дипломы.
Для того чтобы эта конструкция выглядела более красиво,
Петя хочет, чтобы доска была квадратной и занимала как можно меньше места на стене.
Каждый диплом должен быть размещён строго в прямоугольнике размером w на h.
Дипломы запрещается поворачивать на 90 градусов.
Прямоугольники, соответствующие различным дипломам, не должны иметь общих внутренних точек.
Требуется написать программу, которая вычислит минимальный размер стороны доски,
которая потребуется Пете для размещения всех своих дипломов.

Формат ввода
Входной файл содержит три целых числа: w, h, n (1 ≤ w, h, n ≤ 10⁹).

Формат вывода
В выходной файл необходимо вывести ответ на поставленную задачу.
"""
from typing import Callable

MAX_INT = (2 ** 64 - 1) // 2
MIN_INT = -2 ** 64 // 2


def read(name: str = 'input.txt') -> (int, int, int):
    reader = open(name, 'r')
    w, h, n = [int(i) for i in reader.readline().split()]
    reader.close()
    return w, h, n


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write("%d\n" % result)
    writer.close()
    pass


def left_binary_search(left: int, right: int, check: Callable[[int], bool]) -> int:
    if left > right:
        return MIN_INT
    while left < right:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle + 1
    if check(left):
        return left
    return MIN_INT


def check(w: int, h: int, n: int, s: int) -> bool:
    return (s // w) * (s // h) >= n


def solution(inp: tuple[int, int, int]) -> int:
    w, h, n = inp
    return left_binary_search(1, max(n*w, n*h), lambda size: check(w, h, n, size))


class Part6:
    class ProblemC:
        def __init__(self):
            write(solution(read()))


def main():
    Part6.ProblemC()
    pass


if __name__ == "__main__":
    main()
    pass
