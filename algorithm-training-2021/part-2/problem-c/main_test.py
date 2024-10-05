#!/usr/bin/env python3

import main
import unittest


class TestPart2ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual(5, main.part_2_problem_c([1, 2, 3, 4, 5], 6))

    def test_sub_solution_c_case_2(self):
        self.assertEqual(3, main.part_2_problem_c([5, 4, 3, 2, 1], 3))

    def test_sub_solution_c_case_5(self):
        self.assertEqual(24, main.part_2_problem_c([1, 1000, 456, 345, 234, 123, 23, 12, 24, 35], 25))


if __name__ == "__main__":

    unittest.main()
    pass
