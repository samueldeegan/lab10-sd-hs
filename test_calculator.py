import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(0, 1), 0)
        self.assertEqual(calculator.mul(-1, 1), -1)
    def test_divide(self):
        self.assertEqual(calculator.div(2, 3), 1)
        self.assertEqual(calculator.div(0, 1), 0)
        self.assertEqual(calculator.div(-1, 1), -1)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(1), 1)
        self.assertEqual(calculator.square_root(0), 0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()