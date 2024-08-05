import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        self.assertEqual(solution.productExceptSelf(nums), expected)

    def test_2(self):
        solution = Solution()
        nums = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]
        self.assertEqual(solution.productExceptSelf(nums), expected)



if __name__ == '__main__':
    unittest.main()