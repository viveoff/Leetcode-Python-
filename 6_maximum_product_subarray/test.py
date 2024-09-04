import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [-4,-3,-2]
        excepted = 12
        self.assertEqual(solution.maxProduct(nums), excepted)


if __name__ == '__main__':
    unittest.main()