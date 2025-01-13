class Memento:
    """Represents a game save."""
    def __init__(self, state):
        self.state = state

class Caretaker:
    """Manages game state mementos."""
    def __init__(self):
        self.saved_states = []

    def save_state(self, memento):
        """Adds a memento to the list."""
        self.saved_states.append(memento)

    def get_last_state(self):
        """Retrieves the last saved memento."""
        return self.saved_states[-1] if self.saved_states else None