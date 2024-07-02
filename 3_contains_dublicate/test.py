import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [1, 2, 3, 1]
        expected_output = True
        self.assertEqual(solution.containsDuplicate(nums), expected_output)

    def test_case_2(self):
        solution = Solution()
        nums = [1,2,3,4]
        expected_output = False
        self.assertEqual(solution.containsDuplicate(nums), expected_output)

    def test_case_3(self):
        solution = Solution()
        nums = [1,1,1,3,3,4,3,2,4,2]
        expected_output = True
        self.assertEqual(solution.containsDuplicate(nums), expected_output)


if __name__ == '__main__':
    unittest.main()