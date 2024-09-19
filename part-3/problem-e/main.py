#!/usr/bin/env python3

"""
В новой программе OpenCalculator появилась новая возможность – можно настроить,
какие кнопки отображаются, а какие – нет. Если кнопка не отображается на экране,
то ввести соответствующую цифру с клавиатуры или копированием из другой программы нельзя.
Петя настроил калькулятор так, что он отображает только кнопки с цифрами x, y, z.
Напишите программу, определяющую, сможет ли Петя ввести число N, а если нет,
то какое минимальное количество кнопок надо дополнительно отобразить на экране для его ввода.

Формат ввода
Сначала вводятся три различных числа из диапазона от 0 до 9: x, y и z (числа разделяются пробелами). Далее вводится целое неотрицательное число N, которое Петя хочет ввести в калькулятор. Число N не превышает 10000.

Формат вывода
Выведите, какое минимальное количество кнопок должно быть добавлено для того,
чтобы можно было ввести число N
(если число может быть введено с помощью уже имеющихся кнопок, выведите 0)
"""


def read(name: str = 'input.txt') -> (set[int], set[int]):
    reader = open(name, 'r')
    inp1 = set[int]([int(n) for n in reader.readline().split(" ")])
    inp2 = set[int]([int(c) for c in reader.readline().strip() if c.isdigit()])
    print(inp1)
    print(inp2)
    reader.close()
    return inp1, inp2


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write(str(result))
    writer.close()
    pass


def solution(inp: (set[int], set[int])) -> int:
    return len(inp[1].difference(inp[0]))


class Part3:
    class ProblemE:
        def __init__(self):
            write(solution(read()))


def main():
    Part3.ProblemE()
    pass


if __name__ == "__main__":
    main()
    pass
