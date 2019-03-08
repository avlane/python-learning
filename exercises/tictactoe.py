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
