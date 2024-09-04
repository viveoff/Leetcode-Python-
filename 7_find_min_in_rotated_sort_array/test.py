import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [3, 4, 5, 1, 1]
        output = 1
        self.assertEqual(solution.findMin(nums), output)

    def test_2(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        output = 0
        self.assertEqual(solution.findMin(nums), output)
    
    def test_3(self):
        solution = Solution()
        nums = [11,13,15,17]
        output = 11
        self.assertEqual(solution.findMin(nums), output)


if __name__ == '__main__':
    unittest.main()