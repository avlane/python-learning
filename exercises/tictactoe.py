WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def new_board():
    return [" "] * 9


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def render(board):
    rows = []
    for start in (0, 3, 6):
        rows.append(" " + " | ".join(board[start:start + 3]))
    return "\n---+---+---\n".join(rows)


def play(input_fn=input, output_fn=print):
    board = new_board()
    mark = "X"
    for _ in range(9):
        output_fn(render(board))
        square = int(input_fn("{} to move (1-9): ".format(mark)))
        board[square - 1] = mark
        if winner(board):
            output_fn(render(board))
            output_fn("{} wins!".format(mark))
            return mark
        mark = "O" if mark == "X" else "X"
    output_fn("It is a draw.")
    return None


def main():
    play()


if __name__ == "__main__":
    main()
