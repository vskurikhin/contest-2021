#!/usr/bin/env python3

import main
import random
import unittest


def rnd(n: int):
    print("%d" % n)
    for i in range(n):
        print("%d %d" % (random.randrange(1, 4), random.randrange(1, 4)))


def rand():
    rnd(3)
    pass


class TestPart3ProblemsC(unittest.TestCase):

    def test_data(self):
        rand()

    def test_sub_solution_c_case_1(self):
        self.assertEqual(5, main.solution(main.read("input.txt")))

    def test_sub_solution_c_case_1(self):
        self.assertEqual(469, main.solution(main.read("input_test2.txt")))


if __name__ == "__main__":
    unittest.main()
    pass
