import tkinter as tk

from strategy import EasyBoardStrategy
from strategy import MediumBoardStrategy
from strategy import HardBoardStrategy

def create_gui():
    root = tk.Tk()
    root.title("Minesweeper")

    def start_game(strategy):
        size, num_mines = strategy.generate_board()
        print(f"Starting game with size {size}x{size} and {num_mines} mines.")

    tk.Label(root, text="Choose Difficulty:", font=("Arial", 16), pady=10).grid(row=0, column=0, padx=20)

    tk.Button(root, text="Easy", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(EasyBoardStrategy())).grid(row=1, column=0, pady=10)
    tk.Button(root, text="Medium", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(MediumBoardStrategy())).grid(row=2, column=0, pady=10)
    tk.Button(root, text="Hard", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(HardBoardStrategy())).grid(row=3, column=0, pady=10)

    root.mainloop()
