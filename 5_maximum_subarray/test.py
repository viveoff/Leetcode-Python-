import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected = 6
        self.assertEqual(solution.maxSubArray(nums), expected)

    def test_2(self):
        solution = Solution()
        nums = [5,4,-1,7,8]
        expected = 23
        self.assertEqual(solution.maxSubArray(nums), expected)




if __name__ == '__main__':
    unittest.main()