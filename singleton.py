class GameSingleton:
    """Singleton class to manage game."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        import state
        if not cls._instance:
            cls._instance = super(GameSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.board = None
            cls._instance.buttons = None
            cls._instance.remaining_mines = 0
            cls._instance.state = state.PlayingState()
            cls._instance.observers = []
        return cls._instance

    def add_observer(self, observer):
        """Add observer."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Remove observer."""
        self.observers.remove(observer)

    def notify_observers(self):
        """Notify observer."""
        for observer in self.observers:
            observer.update(self)

    def flagged_mine(self):
        self.notify_observers()