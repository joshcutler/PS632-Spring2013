import unittest
import lab3

class TestLab3Code(unittest.TestCase):

    def setUp(self):
        return 

    # correctness tests:

    def test_fizz_buzz_1(self):
        x = lab3.FizzBuzz(1)
        self.assertEqual(x, 1)

    def test_fizz_buzz_3(self):
        x = lab3.FizzBuzz(3)
        self.assertEqual(x, "Fizz")

    def test_fizz_buzz_5(self):
        x = lab3.FizzBuzz(5)
        self.assertEqual(x, "Buzz")

    def test_fizz_buzz_15(self):
        x = lab3.FizzBuzz(15)
        self.assertEqual(x, "FizzBuzz")


    def test_newton_root_4(self):
        root = lab3.NewtonRoot(4)
        self.assertEqual(root, 2.0)

    def test_newton_root_9(self):
        root = lab3.NewtonRoot(9)
        self.assertEqual(root, 3.0)

    def test_newton_root_10(self):
        root = lab3.NewtonRoot(10)
        self.assertAlmostEqual(root, 10**.5)


    def test_gcd1(self):
        denom = lab3.gcd1(54, 72)
        self.assertEqual(denom, 18)

    def test_gcd2(self):
        denom = lab3.gcd2(54, 72)
        self.assertEqual(denom, 18)


if __name__ == '__main__':
    unittest.main()

