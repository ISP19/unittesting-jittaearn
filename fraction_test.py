import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        with self.assertRaises(TypeError):
            Fraction("hi",3)
        with self.assertRaises(TypeError):
            Fraction(2,"Hello")
        with self.assertRaises(TypeError):
            Fraction("bear","wolf")

    def test_str(self):
        #Test the string format of the fraction
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0,10)
        self.assertEqual("0", f.__str__())
        f = Fraction(0,0)
        self.assertEqual("0/0", f.__str__())
        f = Fraction(1,0)
        self.assertEqual("1/0", f.__str__())

    def test_add(self):
        #Test addition of two fraction. Example: 3/4 = 2/3 + 1/12.
        self.assertEqual(Fraction(3,4), Fraction(1,12) + Fraction(2,3))
        self.assertEqual(Fraction(-2,5), Fraction(-1,5) + Fraction(-2,10))
        self.assertEqual(Fraction(1,14), Fraction(4,7) + Fraction(-3,6))
        self.assertEqual(Fraction(-1,8), Fraction(3,8) + Fraction(-1,2))
        self.assertEqual(Fraction(6,20), Fraction(6,20) + Fraction(0))

    def test_sub(self):
        #Test subtraction of two fraction. Example: 1/4 = 1/2 - 1/4.
        self.assertEqual(Fraction(-7,12), Fraction(1,12) - Fraction(2,3))
        self.assertEqual(Fraction(0), Fraction(-1,5) - Fraction(-2,10))
        self.assertEqual(Fraction(15,14), Fraction(4,7) - Fraction(-3,6))
        self.assertEqual(Fraction(7,8), Fraction(3,8) - Fraction(-1,2))
        self.assertEqual(Fraction(11,22), Fraction(11,22) - Fraction(0))

    def test_mul(self):
        #Test the multiplication of two fraction. Example: 8/10 = 4/10 * 2*1
        self.assertEqual(Fraction(3,10), Fraction(1,2)*Fraction(3,5))
        self.assertEqual(Fraction(4,6), Fraction(-4,3)*Fraction(-1,2))
        self.assertEqual(Fraction(-18,28), Fraction(-6,7)*Fraction(3,4))
        self.assertEqual(0, Fraction(0)*Fraction(8,4))

    def test_eq(self):
        #Test if the fractions in simplest form are equal. 
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertNotEqual(Fraction(1,0), Fraction(-1,0))
        self.assertEqual(Fraction(1,0), Fraction(1,0))
        self.assertEqual(Fraction(0), Fraction(0))
        self.assertEqual(Fraction(-1,0), Fraction(-1,0))

    def test_gt(self):
        #Test wheter if the first fraction is greater than the second fraction.
        f = Fraction(1,2)
        g = Fraction(1,4)
        h = Fraction(1,4)
        i = Fraction(3,4)
        self.assertTrue(f.__gt__(g))
        self.assertFalse(f.__gt__(i))
        self.assertFalse(g.__gt__(h))

    def test_neg(self):
        #Test if the fraction is negated.
        self.assertEqual(Fraction(-2,5), -Fraction(2,5))
        self.assertEqual(Fraction(5,12), -Fraction(-5,12))
        self.assertEqual(0, -Fraction(0)) 
        


if __name__ == "__main__":
    """Run the doctests in all methods."""
    unittest.main(verbosity=2)
