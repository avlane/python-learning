import unittest

from exercises.temperature import celsius_to_fahrenheit, convert, fahrenheit_to_celsius


class TemperatureTests(unittest.TestCase):
    def test_freezing(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    def test_boiling(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(fahrenheit_to_celsius(212), 100)

    def test_minus_forty_is_the_same_in_both(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)

    def test_convert_picks_direction(self):
        self.assertEqual(convert(100, "F"), 212)
        self.assertEqual(convert(212, "c"), 100)

    def test_convert_rejects_unknown_unit(self):
        with self.assertRaises(ValueError):
            convert(1, "k")


if __name__ == "__main__":
    unittest.main()
