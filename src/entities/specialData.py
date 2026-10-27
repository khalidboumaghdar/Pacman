class SpecialData:
    """the class that control SpecialData infastructor"""
    def __init__(self, lives: int) -> None:
        """constructor method"""
        self.score = 0
        self.currentLevel = 0
        self.lives = lives
        self.allLevels = 0
