import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        expected_output = 5
        self.assertEqual(solution.maxProfit(prices), expected_output)

    def test_case_2(self):
        solution = Solution()
        prices = prices = [7,6,4,3,1]
        expected_output = 0
        self.assertEqual(solution.maxProfit(prices), expected_output)


if __name__ == '__main__':
    unittest.main()