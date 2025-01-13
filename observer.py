class MinesLabelObserver:
    """Updates the information about mines"""
    def __init__(self, label_widget):
        self.label = label_widget

    def update(self, game):
        self.label["text"] = f"Mines Remaining: {game.remaining_mines}"