class GameSingleton:
    """Singleton class to manage game state."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        import state
        if not cls._instance:
            cls._instance = super(GameSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.board = None
            cls._instance.buttons = None
            cls._instance.remaining_mines = 0
            cls._instance.state = state.PlayingState()
        return cls._instance
    
    def update_mines_label(self):
        if hasattr(self, 'mines_label'):
            self.mines_label.config(text=f"Mines Remaining: {self.remaining_mines}")