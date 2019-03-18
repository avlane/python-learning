WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def new_board():
    return [" "] * 9


def make_move(board, square, mark):
    """Place mark on square 1-9. Raises ValueError if the move is not allowed."""
    if not 1 <= square <= 9:
        raise ValueError("choose a square from 1 to 9")
    if board[square - 1] != " ":
        raise ValueError("square {} is already taken".format(square))
    board[square - 1] = mark


def is_full(board):
    return " " not in board


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
    while not is_full(board):
        output_fn(render(board))
        try:
            make_move(board, int(input_fn("{} to move (1-9): ".format(mark))), mark)
        except ValueError as err:
            output_fn("Sorry, " + str(err) + ".")
            continue
        if winner(board):
            output_fn(render(board))
            output_fn("{} wins!".format(mark))
            return mark
        mark = "O" if mark == "X" else "X"
    output_fn(render(board))
    output_fn("It is a draw.")
    return None


def main():
    play()


if __name__ == "__main__":
    main()
