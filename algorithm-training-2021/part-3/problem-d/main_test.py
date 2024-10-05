#!/usr/bin/env python3

import main
import unittest


class TestPart3ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual([0, 1], main.solution1(({0, 1, 10, 9}, {1, 3, 0})))

    def test_sub_solution_c_case_2(self):
        self.assertEqual([9, 10], main.solution2(({0, 1, 10, 9}, {1, 3, 0})))

    def test_sub_solution_c_negative_case_3(self):
        self.assertEqual([3], main.solution3(({0, 1, 10, 9}, {1, 3, 0})))


if __name__ == "__main__":
    unittest.main()
    pass
