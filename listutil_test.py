import unittest
from listutil import unique


class ListutilTest(unittest.TestCase):
    """Test for unique function."""

    def test_empty_list(self):
        #Return an empty list [].
        self.assertEqual([], unique([]))

    def test_single_item_list(self):
        #Return itself  example: [2] will return [2].
        self.assertEqual([3], unique([3]))
        self.assertEqual(['b'], unique(["b"]))
        self.assertEqual(['A'], unique(["A", "A", "A", "A", "A"]))

    def test_a_large_list(self):
        #Return only one duplicates of each same element.
        self.assertEqual([1, 5, 6, 8, 9, 7, 3, 4, 0, -1, -4, -5, -7, -6], unique([1,5,6,8,9,5,7,7,5,7,9,5,3,4,6,8,6,8,9,0,-1,3,5,-4,9,-5,-7,-6, 5,5,5,5,5,5,5]))

    def test_multiple_item_list(self):
        #Return only one duplicates of each same element.
        self.assertEqual(['h', 'd'], unique(['h','h','d','d','d']))
        self.assertEqual(['hello'], unique(['hello', 'hello', 'hello', 'hello', 'hello']))
        self.assertEqual([1, 2, [3, 3], 4], unique([1, 2, 2, [3, 3], 4, 4]))
        self.assertEqual(['bear', 'apple'], unique(['bear', 'bear', 'apple', 'bear']))

    def test_not_a_list(self):
        #Raises TypeError.
        with self.assertRaises(TypeError):
            unique("hi",3)

if __name__ == "__main__":
    """Run the doctests in all methods."""
    unittest.main()
