import unittest
from candies import candies, candies_optimized

class CandiesTest(unittest.TestCase):
    def test_one_steps(self):
        # Allocation: [1, 2, 1]
        self.assertEqual(candies([1, 2, 1]), 4)
        # Allocation: [1, 2, 1, 2, 1, 2]
        self.assertEqual(candies([2, 4, 1, 10, 2, 4]), 9)
        # Allocation: [1, 2, 1, 2, 1, 2, 1, 2]
        self.assertEqual(candies([2, 4, 3, 5, 2, 6, 4, 5]), 12)
        # Allocation: [2, 1, 2, 1, 2]
        self.assertEqual(candies([4, 1, 10, 2, 78]), 8)

    def test_multiple_mark_descent(self):
        # Allocation: [3, 2, 1, 2, 3]
        self.assertEqual(candies([5, 3, 1, 2, 3]), 11)
        # Allocation: [1, 2, 6, 5, 4, 3, 2, 1]
        self.assertEqual(candies([2, 3, 10, 9, 8, 7, 6, 5]), 24)
        # Allocation: [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(candies([10, 9, 7, 4, 3, 2, 1]), 28)

    def test_simple_contiguously_repeated_marks(self):
        # Allocation: [1, 2, 1]
        self.assertEqual(candies([1, 2, 2]), 4)
        # Allocation: [1, 1, 1, 1, 1]
        self.assertEqual(candies([2, 2, 2, 2, 2]), 5)
        # Allocation: [1, 2, 1, 1, 1]
        self.assertEqual(candies([1, 10, 10, 10, 10]), 6)
        # Allocation: [2, 1, 1, 1, 1]
        self.assertEqual(candies([5, 3, 3, 3, 3]), 6)
        # Allocation: [3, 2, 1, 2, 1, 2]
        self.assertEqual(candies([6, 5, 1, 2, 2, 3]), 11)

    def test_more_than_two_jump_in_allocations(self):
        # Allocation: [1, 2, 3, 1]
        self.assertEqual(candies([1, 2, 3, 1]), 7)
        # Allocation: [3, 2, 1, 1, 3, 2, 1]
        self.assertEqual(candies([5, 3, 1, 6, 6, 2, 1]), 14) # This one is a tricky one!
        # Allocation: [1, 2, 3, 4, 5, 2, 1]
        self.assertEqual(candies([1, 2, 3, 4, 100, 2, 1]), 18)
        # Allocation: [1, 2, 1, 2, 1, 2, 3, 4, 2, 1]
        self.assertEqual(candies([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]), 19)

    def test_no_marks(self):
        self.assertEqual(candies([]), 0)

    def test_one_mark(self):
        # All allocations: [1]
        self.assertEqual(candies([1]), 1)
        self.assertEqual(candies([2374875]), 1)

class CandiesOptimizedTest(unittest.TestCase):
    def test_one_steps(self):
        # Allocation: [1, 2, 1]
        self.assertEqual(candies_optimized([1, 2, 1]), 4)
        # Allocation: [1, 2, 1, 2, 1, 2]
        self.assertEqual(candies_optimized([2, 4, 1, 10, 2, 4]), 9)
        # Allocation: [1, 2, 1, 2, 1, 2, 1, 2]
        self.assertEqual(candies_optimized([2, 4, 3, 5, 2, 6, 4, 5]), 12)
        # Allocation: [2, 1, 2, 1, 2]
        self.assertEqual(candies_optimized([4, 1, 10, 2, 78]), 8)

    def test_multiple_mark_descent(self):
        # Allocation: [3, 2, 1, 2, 3]
        self.assertEqual(candies_optimized([5, 3, 1, 2, 3]), 11)
        # Allocation: [1, 2, 6, 5, 4, 3, 2, 1]
        self.assertEqual(candies_optimized([2, 3, 10, 9, 8, 7, 6, 5]), 24)
        # Allocation: [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(candies_optimized([10, 9, 7, 4, 3, 2, 1]), 28)

    def test_simple_contiguously_repeated_marks(self):
        # Allocation: [1, 2, 1]
        self.assertEqual(candies_optimized([1, 2, 2]), 4)
        # Allocation: [1, 1, 1, 1, 1]
        self.assertEqual(candies_optimized([2, 2, 2, 2, 2]), 5)
        # Allocation: [1, 2, 1, 1, 1]
        self.assertEqual(candies_optimized([1, 10, 10, 10, 10]), 6)
        # Allocation: [2, 1, 1, 1, 1]
        self.assertEqual(candies_optimized([5, 3, 3, 3, 3]), 6)
        # Allocation: [3, 2, 1, 2, 1, 2]
        self.assertEqual(candies_optimized([6, 5, 1, 2, 2, 3]), 11)

    def test_more_than_two_jump_in_allocations(self):
        # Allocation: [1, 2, 3, 1]
        self.assertEqual(candies_optimized([1, 2, 3, 1]), 7)
        # Allocation: [3, 2, 1, 1, 3, 2, 1]
        self.assertEqual(candies_optimized([5, 3, 1, 6, 6, 2, 1]), 14) # This one is a tricky one!
        # Allocation: [1, 2, 3, 4, 5, 2, 1]
        self.assertEqual(candies_optimized([1, 2, 3, 4, 100, 2, 1]), 18)
        # Allocation: [1, 2, 1, 2, 1, 2, 3, 4, 2, 1]
        self.assertEqual(candies_optimized([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]), 19)

    def test_no_marks(self):
        self.assertEqual(candies_optimized([]), 0)

    def test_one_mark(self):
        # All allocations: [1]
        self.assertEqual(candies_optimized([1]), 1)
        self.assertEqual(candies_optimized([2374875]), 1)
