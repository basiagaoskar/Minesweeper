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