#!/usr/bin/env python3

import main
import unittest


class TestPart3ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual((2, 1), main.solution(main.read("input.txt")))

    def test_sub_solution_c_case_2(self):
        self.assertEqual((4, 1), main.solution(main.read("input_test2.txt")))

    def test_sub_solution_c_case_3(self):
        self.assertEqual((10, 1), main.solution(main.read("input_test3.txt")))

    def test_sub_solution_c_case_5(self):
        self.assertEqual((10, 1), main.solution(main.read("input_test5.txt")))


if __name__ == "__main__":
    unittest.main()
    pass
