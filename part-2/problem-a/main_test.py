#!/usr/bin/env python3

import main
import unittest


class TestPart2ProblemsA(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertTrue(main.part_2_solution_a([0]))

    def test_sub_solution_c_case_2(self):
        self.assertTrue(main.part_2_solution_a([0, 1]))

    def test_sub_solution_c_negative_case_3(self):
        self.assertFalse(main.part_2_solution_a([0, 0]))


if __name__ == "__main__":

    unittest.main()
    pass
