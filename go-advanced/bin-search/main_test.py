#!/usr/bin/env python3

import main
import unittest


class TestPart2ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        print(main.part_2_problem_c([4, 6, 0, 1, 7, 3, 5, 2], 3))


if __name__ == "__main__":

    unittest.main()
    pass
