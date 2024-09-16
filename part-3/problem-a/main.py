#!/usr/bin/env python3

"""
Дан список чисел, который может содержать до 100000 чисел.
Определите, сколько в нем встречается различных чисел. 
"""


def read(name: str = 'input.txt') -> list[int]:
    reader = open(name, 'r')
    result = [int(n) for n in reader.readline().split(" ")]
    reader.close()
    return result


def write(result: int, name: str = 'output.txt') -> None:
    writer = open(name, 'w')
    writer.write(str(result))
    pass


def solution(inp: list[int]) -> int:
    m = dict[int, int]()
    for value in inp:
        m.setdefault(value, 0)
    return len(m)


class Part3:
    class ProblemA:
        def __init__(self):
            write(solution(read()))


def main():
    Part3.ProblemA()
    pass


if __name__ == "__main__":
    main()
    pass
