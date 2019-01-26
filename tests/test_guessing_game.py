import unittest

from exercises.guessing_game import play


def scripted(answers):
    it = iter(answers)
    return lambda prompt: next(it)


class GuessingGameTests(unittest.TestCase):
    def run_game(self, secret, answers, **kwargs):
        lines = []
        won = play(secret, scripted(answers), lines.append, **kwargs)
        return won, lines

    def test_win_on_first_guess(self):
        won, lines = self.run_game(42, ["42"])
        self.assertTrue(won)
        self.assertIn("You got it in 1 tries!", lines)

    def test_hints(self):
        won, lines = self.run_game(42, ["10", "90", "42"])
        self.assertTrue(won)
        self.assertEqual(lines[1:3], ["Too low", "Too high"])

    def test_runs_out_of_attempts(self):
        won, lines = self.run_game(7, ["1", "2", "3"], max_attempts=3)
        self.assertFalse(won)
        self.assertEqual(lines[-1], "Out of tries. The number was 7.")

    def test_non_numbers_are_rejected(self):
        won, lines = self.run_game(5, ["abc", "5"])
        self.assertTrue(won)
        self.assertIn("Please type a whole number.", lines)


if __name__ == "__main__":
    unittest.main()
