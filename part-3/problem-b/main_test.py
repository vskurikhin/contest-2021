#!/usr/bin/env python3

import main
import unittest


class TestPart3ProblemsA(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual(3, main.solution([1, 2, 3, 2, 1]))

    def test_sub_solution_c_case_2(self):
        self.assertEqual(10, main.solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_sub_solution_c_negative_case_3(self):
        self.assertEqual(6, main.solution([1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3]))


if __name__ == "__main__":
    unittest.main()
    pass
