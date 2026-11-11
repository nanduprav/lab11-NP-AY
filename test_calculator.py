# https://github.com/nanduprav/lab11-NP-AY
# Partner 1: Nandana Praveen
# Partner 2: Angela Yang
# Partner 3: Keysie Perez Barriga

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(.5, .5), 1)

    def test_subtract(self): # 3 assertions
    #     fill in code
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(-5, 5), -10)
        self.assertEqual(subtract(.5, .5), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual (mul(.5,40), 20)
        self.assertEqual (mul(-1,-50000), 50000)
        self.assertEqual (mul(-1, 0), 0)


    #     fill in code

    def test_divide(self):
        self.assertEqual (div(2, 2), 1)
        self.assertEqual (div(2, 1), .5)
        self.assertEqual (div(.5, 1000), 2000)

        # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
            with self.assertRaises(ZeroDivisionError):
                div (0, 5)

    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual (logarithm(2, 16), 4)
        self.assertAlmostEqual (logarithm(10, 10), 1)
        self.assertAlmostEqual (logarithm(10, 100), 2)

    #     fill in code

    def test_log_invalid_base(self): # 1 assertion

    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm (5, 0)
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
         with self.assertRaises(ValueError):
              logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions

        self.assertAlmostEqual (hypotenuse(3, 4), 5)
        self.assertAlmostEqual (hypotenuse(5, 12), 13)
        self.assertAlmostEqual (hypotenuse(6, 8), 10)

    #     fill in code

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
         with self.assertRaises(ValueError):
            square_root(-1)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
      unittest.main()