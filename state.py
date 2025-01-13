import tkinter as tk
from singleton import GameSingleton
from board import reveal_board

class GameState:
    """Game state interface."""
    def handle_click(self, x, y):
        pass

    def handle_right_click(self, x, y):
        pass

class PlayingState(GameState):
    """Game state while the game is in progress."""
    def handle_click(self, x, y):
        game = GameSingleton()
        if game.board[x][y] == 'M':
            game.state = GameOverState()
            game.state.handle_click(x, y)
        else:
            reveal_board(game.board, game.buttons, x, y)
            if all(
                game.buttons[i][j]["state"] == "disabled" or game.board[i][j] == 'M'
                for i in range(len(game.board))
                for j in range(len(game.board))
            ):
                game.state = VictoryState()
                game.state.handle_click(x, y)

    def handle_right_click(self, x, y):
        game = GameSingleton()
        button = game.buttons[x][y]
        if button["state"] == "normal":
            if button["text"] == "⚫":
                button["text"] = ""
                game.remaining_mines += 1
            else:
                button["text"] = "⚫"
                game.remaining_mines -= 1
            game.update_mines_label()

class GameOverState(GameState):
    """Game state after lossing."""
    def handle_click(self, x, y):
        game = GameSingleton()
        for i in range(len(game.board)):
            for j in range(len(game.board)):
                if game.board[i][j] == 'M':
                    game.buttons[i][j]["text"] = 'M'
                game.buttons[i][j]["state"] = "disabled"
                game.buttons[i][j]["bg"] = "#d3d3d3"
        tk.messagebox.showinfo("Game Over", "You hit a mine!")

    def handle_right_click(self, x, y):
        tk.messagebox.showinfo("Game Over", "You can't mark cells after the game is over.")

class VictoryState(GameState):
    """Game state after winning."""
    def handle_click(self, x, y):
        tk.messagebox.showinfo("Congratulations", "You cleared the board!")

    def handle_right_click(self, x, y):
        tk.messagebox.showinfo("Victory", "You can't mark cells after winning the game.")
