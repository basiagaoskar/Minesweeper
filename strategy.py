class BoardGenerationStrategy:
    """Board generation strategy interface."""
    def generate_board(self):
        pass

class EasyBoardStrategy(BoardGenerationStrategy):
    """Strategy for easy level."""
    def generate_board(self):
        return 8, 10

class MediumBoardStrategy(BoardGenerationStrategy):
    """Strategy for medium level."""
    def generate_board(self):
        return 12, 24

class HardBoardStrategy(BoardGenerationStrategy):
    """Strategy for hard level."""
    def generate_board(self):
        return 16, 40
