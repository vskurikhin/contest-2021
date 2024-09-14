#!/usr/bin/env python3

import unittest


class TestProblemsC(unittest.TestCase):

    def test_sub_solution_c_case_1(self):
        self.assertEqual(4302397, sub_solution_c("8(495)430-23-97"))
        self.assertEqual(4302397, sub_solution_c("+7-4-9-5-43-023-97"))
        self.assertEqual(4302397, sub_solution_c("4-3-0-2-3-9-7"))
        self.assertEqual(8495430, sub_solution_c("8-495-430"))
        self.assertEqual(8047952807, sub_solution_c("+78047952807"))


if __name__ == "__main__":
    unittest.main()
    pass
