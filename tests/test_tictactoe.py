import unittest

from exercises.tictactoe import new_board, play, render, winner


def board_from(text):
    return list(text.replace("/", ""))


class WinnerTests(unittest.TestCase):
    def test_empty_board_has_no_winner(self):
        self.assertIsNone(winner(new_board()))

    def test_rows_columns_and_diagonals(self):
        self.assertEqual(winner(board_from("XXX/OO /   ")), "X")
        self.assertEqual(winner(board_from("O X/O X/O  ")), "O")
        self.assertEqual(winner(board_from("X O/ XO/  X")), "X")
        self.assertEqual(winner(board_from("  O/ O /O  ")), "O")

    def test_no_winner_mid_game(self):
        self.assertIsNone(winner(board_from("XO /OX /   ")))


class RenderTests(unittest.TestCase):
    def test_render(self):
        text = render(board_from("XO /   /  X"))
        self.assertEqual(text.splitlines()[0], " X | O |  ")
        self.assertEqual(len(text.splitlines()), 5)


class GameTests(unittest.TestCase):
    def test_x_wins_along_the_top(self):
        moves = iter(["1", "4", "2", "5", "3"])
        lines = []
        result = play(lambda prompt: next(moves), lines.append)
        self.assertEqual(result, "X")
        self.assertEqual(lines[-1], "X wins!")


if __name__ == "__main__":
    unittest.main()
