import tkinter as tk

from strategy import EasyBoardStrategy
from strategy import MediumBoardStrategy
from strategy import HardBoardStrategy

from singleton import GameSingleton
from board import generate_board

def create_gui():
    root = tk.Tk()
    root.title("Minesweeper")

    def start_game(strategy):
        for widget in root.winfo_children():
            widget.destroy()
        create_game(root, strategy)

    tk.Label(root, text="Choose Difficulty:", font=("Arial", 16), pady=10).grid(row=0, column=0, padx=20)

    tk.Button(root, text="Easy", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(EasyBoardStrategy())).grid(row=1, column=0, pady=10)
    tk.Button(root, text="Medium", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(MediumBoardStrategy())).grid(row=2, column=0, pady=10)
    tk.Button(root, text="Hard", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(HardBoardStrategy())).grid(row=3, column=0, pady=10)

    root.mainloop()

def create_game(root, strategy):
    """Initializes the game in the window."""
    size, num_mines = strategy.generate_board()
    game = GameSingleton()
    game.board = generate_board(size, num_mines)
    game.remaining_mines = num_mines


    game.buttons = [[None for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            btn = tk.Button(root, text="", width=3, height=1)
            btn.grid(row=i, column=j)
            game.buttons[i][j] = btn