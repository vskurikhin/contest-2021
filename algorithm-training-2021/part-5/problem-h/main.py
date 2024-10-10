#!/usr/bin/env python3

"""
"""
from typing import TextIO

MIN_INT = -((2 ** 64) // 2)


def read(name: str = 'input.txt', inp: TextIO = None) -> tuple[int, int, str]:
    reader = inp if inp is not None else open(name, 'r')
    n, k = [int(i) for i in reader.readline().split()]
    s = reader.readline().strip()
    reader.close()
    return n, k, s


def write(result: tuple[int, int], name: str = 'output.txt', out: TextIO = None) -> None:
    writer = out if out is not None else open(name, 'w')
    writer.write("%d %d\n" % (result[0], result[1]))
    writer.close()
    pass


def solution(inp: tuple[int, int, str]) -> tuple[int, int]:
    n, k, s = inp
    d = dict[chr, int]()
    rs = list[tuple[int, int]]()
    j = 0
    for i in range(len(s)):
        c = s[i]
        count = d.get(c)
        if count is not None:
            count += 1
        else:
            count = 1
        print("i: ", i, "j: ", j, "c: ", c, ", count: ", count)
        if count > k:
            print("i - j: %d, j + 1: %d" % (i - j, j + 1))
            rs.append((i - j, j + 1))
            d = dict[chr, int]()
            j = i
        else:
            d[c] = count
    if len(rs) == 0:
        rs.append((n, 1))
    r = tuple((MIN_INT, 0))
    for v in rs:
        if v[0] > r[0]:
            r = v
    return r


class Part5:
    class ProblemH:
        def __init__(self):
            write(solution(read()))


def main():
    Part5.ProblemH()
    pass


if __name__ == "__main__":
    main()
    pass
