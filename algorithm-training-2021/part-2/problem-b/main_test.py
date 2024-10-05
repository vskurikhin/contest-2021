#!/usr/bin/env python3

import main
import unittest


class TestPart2ProblemsA(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        for i in range(10):
            self.assertEqual("CONSTANT", main.part_2_solution_b(i, i, ""))

    def test_sub_solution_c_case_2(self):
        for i in range(10):
            self.assertEqual("ASCENDING", main.part_2_solution_b(i-1, i, ""))

    def test_sub_solution_c_case_3(self):
        for i in range(10):
            self.assertEqual("ASCENDING", main.part_2_solution_b(i-1, i, "ASCENDING"))

    def test_sub_solution_c_case_4(self):
        for i in range(10):
            self.assertEqual("DESCENDING", main.part_2_solution_b(i+1, i, ""))

    def test_sub_solution_c_case_5(self):
        for i in range(10):
            self.assertEqual("DESCENDING", main.part_2_solution_b(i+1, i, "DESCENDING"))


if __name__ == "__main__":

    unittest.main()
    pass
