import unittest
from maxSubsetSum import maxSubsetSum

class MaxSubsetSumTest(unittest.TestCase):
    def test_magnitudes_of_one(self):
        self.assertEqual(maxSubsetSum([1, 1, 1, 1, 1, 1]), 3)
        self.assertEqual(maxSubsetSum([-1, 1, -1, 1, -1, 1, -1]), 3)
        self.assertEqual(maxSubsetSum([-1, 1, 1, -1, 1]), 2)
        self.assertEqual(maxSubsetSum([1, -1, -1, 1, 1]), 2)

    def test_all_positive(self):
        self.assertEqual(maxSubsetSum([3, 7, 4, 6, 5]), 13)
        self.assertEqual(maxSubsetSum([2, 1, 5, 8, 4]), 11)

    def test_mix_signs(self):
        self.assertEqual(maxSubsetSum([3, 5, -7, 8, 10]), 15)
        self.assertEqual(maxSubsetSum([3, -5, -7, 8, 10]), 13)

    def test_slightly_complicated(self):
        self.assertEqual(maxSubsetSum([5, 1, 5, 1, 5, -1, -1, -1, 10]), 25)

    def test_thicc_gaps(self):
        self.assertEqual(maxSubsetSum([10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5]), 15)
        self.assertEqual(maxSubsetSum([10, -1, -1, -1, -1123, -1, -1, -1, -25, -1, 1245, -1, -1, -1, -12, -1, -1, -1, -1, -1, 5]), 1260)

    def test_all_negative(self):
        self.assertEqual(maxSubsetSum([-2, -3, -1, -15]), 0)

    def test_short_cases(self):
        self.assertEqual(maxSubsetSum([2]), 2)
        self.assertEqual(maxSubsetSum([1, 2]), 2)

    def test_empty_case(self):
        self.assertEqual(maxSubsetSum([]), 0)
