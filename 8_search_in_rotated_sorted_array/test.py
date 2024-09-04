# python3 -m unittest discover

import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 0
        output = 4
        self.assertEqual(solution.search(nums, target), output)
    
    def test_2(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 3
        output = -1
        self.assertEqual(solution.search(nums, target), output)
    
    def test_3(self):
        solution = Solution()
        nums = [1]
        target = 0
        output = -1
        self.assertEqual(solution.search(nums, target), output)

if __name__ == '__main__':
    unittest.main()


