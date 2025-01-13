import tkinter as tk
import strategy
import state
from singleton import GameSingleton
from board import generate_board
from observer import MinesLabelObserver
from memento import Memento

def create_gui(root=None):
    if root is None:
        root = tk.Tk()
        root.title("Minesweeper")
    
    def start_game(strategy):
        for widget in root.winfo_children():
            widget.destroy()
        create_game(root, strategy)

    tk.Label(root, text="Choose Difficulty:", font=("Arial", 16), pady=10).grid(row=0, column=0, padx=20)

    tk.Button(root, text="Easy", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(strategy.EasyBoardStrategy())).grid(row=1, column=0, pady=10)
    tk.Button(root, text="Medium", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(strategy.MediumBoardStrategy())).grid(row=2, column=0, pady=10)
    tk.Button(root, text="Hard", font=("Arial", 14), width=15, height=2,
              command=lambda: start_game(strategy.HardBoardStrategy())).grid(row=3, column=0, pady=10)

    root.mainloop()

def create_game(root, strategy):
    """Initializes the game in the window."""
    size, num_mines = strategy.generate_board()
    game = GameSingleton()
    game.board = generate_board(size, num_mines)
    game.remaining_mines = num_mines
    game.state = state.PlayingState()

    game.buttons = [[None for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            btn = tk.Button(root, text="", width=3, height=1, command=lambda x=i, y=j: on_click(x, y))
            btn.grid(row=i, column=j)
            btn.bind("<Button-3>", lambda event, x=i, y=j: on_right_click(x, y))
            game.buttons[i][j] = btn
    
    mines_label = tk.Label(root, text=f"Mines Remaining: {num_mines}")
    mines_label.grid(row=size, column=0, columnspan=size)

    observer = MinesLabelObserver(mines_label)
    game.add_observer(observer)

    menu = tk.Menu(root)
    root.config(menu=menu)
    game_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Menu", menu=game_menu)
    game_menu.add_command(label="New Game", command=lambda: restart_game(root))
    game_menu.add_command(label="Save Game", command=lambda: save_game(game))
    game_menu.add_command(label="Load Game", command=lambda: load_game(game))

def on_click(x, y):
    game = GameSingleton()
    game.state.handle_click(x, y)

def on_right_click(x, y):
    game = GameSingleton()
    game.state.handle_right_click(x, y)

def restart_game(root):
    for widget in root.winfo_children():
        widget.destroy()

    game = GameSingleton()
    for observer in game.observers[:]:
        game.remove_observer(observer)
        
    create_gui(root)

def save_game(game):
    game_state = {
        "board": game.board,
        "remaining_mines": game.remaining_mines,
        "buttons_state": [[(btn["state"], btn["text"], btn["bg"]) for btn in row] for row in game.buttons],
        "state": game.state,
    }
    memento = Memento(game_state)
    game.caretaker.save_state(memento)
    tk.messagebox.showinfo("Save Game", "Game saved successfully!")

def load_game(game):
    memento = game.caretaker.get_last_state()
    if memento:
        state = memento.state
        saved_size = len(state["board"])
        current_size = len(game.board) if game.board else 0

        if saved_size != current_size:
            tk.messagebox.showwarning(
                "Load Game", f"Saved board size ({saved_size}x{saved_size}) does not match the current board size ({current_size}x{current_size})."
            )
            return

        game.board = state["board"]
        game.remaining_mines = state["remaining_mines"]
        game.state = state["state"]

        for i, row in enumerate(state["buttons_state"]):
            for j, (btn_state, btn_text, btn_bg) in enumerate(row):
                btn = game.buttons[i][j]
                btn["state"] = btn_state
                btn["text"] = btn_text
                btn["bg"] = btn_bg

        game.notify_observers()

        tk.messagebox.showinfo("Load Game", "Game loaded successfully!")
    else:
        tk.messagebox.showinfo("Load Game", "No saved game available.")