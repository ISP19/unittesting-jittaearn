import math 

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """ 
        gcd = math.gcd(numerator, denominator)
        self.numerator = int(numerator/gcd)
        self.denominator = int(denominator/gcd)
        if self.denominator < 0:
            self.numerator = self.numerator*-1
            self.denominator = self.denominator*-1

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_numerator =  (self.numerator*frac.denominator + self.denominator*frac.numerator)
        new_denominator = self.denominator*frac.denominator
        return Fraction(new_numerator,new_denominator)

    def __str__(self):
        """Return the string of the fraction in the simpliest from.
        """
        if self.denominator == 1:
            return f'{self.numerator}'
        else:
            return f'{self.numerator}/{self.denominator}'

    def __mul__(self, frac):
        """Return the multiplication of two fractions as a new fraction.
        """
        mul_numerator = self.numerator*frac.numerator
        mul_denominator = self.denominator*frac.denominator
        return Fraction(mul_numerator, mul_denominator)

        


    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
   #Optional  have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)``

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator