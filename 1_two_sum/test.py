import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(solution.twoSum(nums, target), expected_output)

    def test_example2(self):
        solution = Solution()
        nums = [3, 2, 4]
        target = 6
        expected_output = [1, 2]
        self.assertEqual(solution.twoSum(nums, target), expected_output)

    def test_example3(self):
        solution = Solution()
        nums = [3, 3]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(solution.twoSum(nums, target), expected_output)

if __name__ == '__main__':
    unittest.main()
