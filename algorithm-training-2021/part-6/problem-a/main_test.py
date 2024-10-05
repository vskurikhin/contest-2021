#!/usr/bin/env python3

import main
import unittest


class TestPart3ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual([False, True, True, True, False, False, True, True, False, True], main.solution(main.read("input.txt")))

    def test_sub_solution_c_case_2(self):
        self.assertEqual([False, True, False, True, True, True, True, False, True, True], main.solution(main.read("input_test2.txt")))

    def test_sub_solution_c_case_3(self):
        self.assertEqual([False, False, True, True, False], main.solution(main.read("input_test3.txt")))


if __name__ == "__main__":
    unittest.main()
    pass
