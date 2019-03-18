import unittest

from exercises.tictactoe import is_full, make_move, new_board, play, render, winner


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


class MoveTests(unittest.TestCase):
    def test_make_move(self):
        board = new_board()
        make_move(board, 5, "X")
        self.assertEqual(board[4], "X")

    def test_rejects_taken_and_out_of_range(self):
        board = new_board()
        make_move(board, 1, "X")
        with self.assertRaises(ValueError):
            make_move(board, 1, "O")
        with self.assertRaises(ValueError):
            make_move(board, 10, "O")

    def test_is_full(self):
        self.assertFalse(is_full(new_board()))
        self.assertTrue(is_full(list("XOXOXOOXO")))


class GameTests(unittest.TestCase):
    def test_draw(self):
        moves = iter("1 2 3 5 4 6 8 7 9".split())
        lines = []
        self.assertIsNone(play(lambda prompt: next(moves), lines.append))
        self.assertEqual(lines[-1], "It is a draw.")

    def test_taken_square_is_refused_without_losing_the_turn(self):
        moves = iter(["1", "1", "4", "2", "5", "3"])
        lines = []
        result = play(lambda prompt: next(moves), lines.append)
        self.assertEqual(result, "X")
        self.assertIn("Sorry, square 1 is already taken.", lines)

    def test_x_wins_along_the_top(self):
        moves = iter(["1", "4", "2", "5", "3"])
        lines = []
        result = play(lambda prompt: next(moves), lines.append)
        self.assertEqual(result, "X")
        self.assertEqual(lines[-1], "X wins!")


if __name__ == "__main__":
    unittest.main()
