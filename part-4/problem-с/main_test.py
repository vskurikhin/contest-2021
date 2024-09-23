#!/usr/bin/env python3

import main
import unittest


class TestPart3ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual("banana", main.solution(main.read("input_test1.txt")))

    def test_sub_solution_c_case_2(self):
        self.assertEqual("ding", main.solution(main.read("input_test2.txt")))

    def test_sub_solution_c_case_3(self):
        self.assertEqual("a", main.solution(main.read("input_test3.txt")))


if __name__ == "__main__":
    unittest.main()
    pass
