#!/usr/bin/env python3

import main
import unittest


class TestPart2ProblemsD(unittest.TestCase):

    def test_sub_solution_d_case_1(self):
        self.assertEqual(0, main.part_2_problem_d([1, 2, 3, 4, 5]))

    def test_sub_solution_d_case_2(self):
        self.assertEqual(0, main.part_2_problem_d([5, 4, 3, 2, 1]))

    def test_sub_solution_d_case_3(self):
        self.assertEqual(2, main.part_2_problem_d([1, 5, 1, 5, 1]))


if __name__ == "__main__":
    unittest.main()
    pass
