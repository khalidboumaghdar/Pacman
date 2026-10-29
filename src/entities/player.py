from src.entities.entity import Entity


class Player:
    """a class that control the palyer infastructor"""
    def __init__(self, entity: Entity):
        """constructor method"""
        self.entity = entity
        self.currentX = self.entity.entityOriginalX
        self.currentY = self.entity.entityOriginalY
        self.nextDirection = "None"
        self.previousDirection = "None"
        self.ignoredDirection = "None"
