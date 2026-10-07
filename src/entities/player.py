from typing import Any


class Player:
    def __init__(self, entity: Any):
        self.entity = entity
        self.currentX = self.entity.entityOriginalX
        self.currentY = self.entity.entityOriginalY
        self.nextDirection = "None"
        self.previousDirection = "None"
        self.ignoredDirection = "None"