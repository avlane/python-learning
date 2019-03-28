import unittest

from exercises.primes import is_prime, primes_up_to


class PrimeTests(unittest.TestCase):
    def test_small_limits(self):
        self.assertEqual(primes_up_to(1), [])
        self.assertEqual(primes_up_to(2), [2])
        self.assertEqual(primes_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_limit_is_inclusive(self):
        self.assertEqual(primes_up_to(13)[-1], 13)

    def test_sieve_agrees_with_trial_division(self):
        self.assertEqual(primes_up_to(500), [n for n in range(501) if is_prime(n)])

    def test_is_prime_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(9))


if __name__ == "__main__":
    unittest.main()
