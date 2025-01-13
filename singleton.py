class GameSingleton:
    """Singleton class to manage game state."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.board = None
            cls._instance.buttons = None
            cls._instance.remaining_mines = 0
        return cls._instance