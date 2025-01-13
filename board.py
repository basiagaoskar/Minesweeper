import random

def generate_board(size, num_mines):
    """Generates a game board with mines."""
    board = [[0 for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < num_mines:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in mines:
            mines.add((x, y))
            board[x][y] = 'M'

            for i in range(max(0, x - 1), min(size, x + 2)):
                for j in range(max(0, y - 1), min(size, y + 2)):
                    if board[i][j] != 'M':
                        board[i][j] += 1
    return board

def reveal_board(board, buttons, x, y):
    """Reveals a cell and its neighbors if it's a zero."""
    size = len(board)
    if x < 0 or x >= size or y < 0 or y >= size or buttons[x][y]["state"] == "disabled":
        return

    buttons[x][y]["text"] = board[x][y] if board[x][y] != 0 else ""
    buttons[x][y]["state"] = "disabled"
    buttons[x][y]["bg"] = "#d3d3d3"

    if board[x][y] == 0:
        for i in range(max(0, x - 1), min(size, x + 2)):
            for j in range(max(0, y - 1), min(size, y + 2)):
                reveal_board(board, buttons, i, j)