from src.entities.entity import Entity


class Player:
    def __init__(self, entity: Entity):
        self.entity = entity
        self.currentX = self.entity.entityOriginalX
        self.currentY = self.entity.entityOriginalY
        self.nextDirection = "None"
        self.previousDirection = "None"
        self.ignoredDirection = "None"
