#!/usr/bin/env python3

import main
import unittest


class TestPart3ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual([1, 3, 7, 1, 5], main.solution(main.read("input.txt")))

    def test_sub_solution_c_case_2(self):
        self.assertEqual([1, 1, 4, 4, 4, 4, 8, 8, 8, 8, 120], main.solution(main.read("input_test2.txt")))

    def test_sub_solution_c_case_3(self):
        self.assertEqual([1, 3, 8, -5, 16, 12, 1, 12, 16, 8], main.solution(main.read("input_test3.txt")))


if __name__ == "__main__":
    unittest.main()
    pass
