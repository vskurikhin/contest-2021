#!/usr/bin/env python3

import main
import unittest


class TestPart3ProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual([1, 4, 6, 8], main.solution(main.read("input.txt")))


if __name__ == "__main__":
    unittest.main()
    pass
