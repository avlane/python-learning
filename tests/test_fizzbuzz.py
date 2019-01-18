import unittest

from exercises.fizzbuzz import fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_plain_numbers(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(4), "4")

    def test_multiples(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
