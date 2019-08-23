import unittest
from listutil import *


class ListutilTest(unittest.TestCase):

    def test_empty_list(self):
        #return an empty list []
        self.assertEqual([], unique([]))

    def test_single_item_list(self):
        #return itself  example: [2] will return [2]
        self.assertEqual([3], unique([3]))
        self.assertEqual(['b'], unique(["b"]))
        self.assertEqual(['A'], unique(["A", "A", "A", "A", "A"]))

    def test_large_list(self):
        #
        pass

    def test_multiple_item_list(self):
        #return only one duplicates of each same element
        self.assertEqual(['h', 'd'], unique(['h','h','d','d','d']))
        self.assertEqual(['hello'], unique(['hello', 'hello', 'hello', 'hello', 'hello']))
        self.assertEqual([1, 2, [3, 3], 4], unique([1, 2, 2, [3, 3], 4, 4]))
        self.assertEqual(['bear', 'apple'], unique(['bear', 'bear', 'apple', 'bear']))

    def test_not_a_list(self):
        #raises TypeError
        with self.assertRaises(TypeError):
            uni = unique('str')


if __name__ == "__main__":
    """Run the doctests in all methods."""
    unittest.main()
