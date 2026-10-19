from src.entities.entity import Entity
from typing import Any


class Ghost:
    def __init__(
        self,
        pinkyEntity: Entity,
        blinkyEntity: Entity,
        inkyEntity: Entity,
        clydeEntity: Entity
    ) -> None:
        self.pinkyEntity = pinkyEntity
        self.blinkyEntity = blinkyEntity
        self.inkyEntity = inkyEntity
        self.clydeEntity = clydeEntity
        self.pinkyCurrentX = \
            self.pinkyEntity.entityOriginalX
        self.pinkyCurrentY = \
            self.pinkyEntity.entityOriginalY
        self.blinkyCurrentX = \
            self.blinkyEntity.entityOriginalX
        self.blinkyCurrentY = \
            self.blinkyEntity.entityOriginalY
        self.inkyCurrentX = self.inkyEntity.entityOriginalX
        self.inkyCurrentY = self.inkyEntity.entityOriginalY
        self.clydeCurrentX = self.clydeEntity.entityOriginalX
        self.clydeCurrentY = self.clydeEntity.entityOriginalY
        self.pinkyPossibleMoves: list = []
        self.blinkyPossibleMoves: list = []
        self.inkyPossibleMoves: list = []
        self.clydePossibleMoves: list = []
        self.frightenedCounter = 0
        self.chaseCounter = 0
        self.currentPinkyMode = "SCATTER"
        self.currentBlinkyMode = "SCATTER"
        self.currentInkyMode = "SCATTER"
        self.currentClydeMode = "SCATTER"
        self.previousPinkyMode = "None"
        self.previousBlinkyMode = "None"
        self.previousInkyMode = "None"
        self.previousClydeMode = "None"
        self.previousPinkyCounterValue = -1
        self.previousBlinkyCounterValue = -1
        self.previousInkyCounterValue = -1
        self.previousClydeCounterValue = -1
        self.previousPinkyX = -1
        self.previousPinkyY = -1
        self.previousBlinkyX = -1
        self.previousBlinkyY = -1
        self.previousInkyX = -1
        self.previousInkyY = -1
        self.previousClydeX = -1
        self.previousClydeY = -1
        self.pinkyCounter = 0
        self.blinkyCounter = 0
        self.inkyCounter = 0
        self.clydeCounter = 0

    def prepareGhostsPossibleMoves(self, grid: list) -> None:
        self.pinkyPossibleMoves = []
        self.blinkyPossibleMoves = []
        self.inkyPossibleMoves = []
        self.clydePossibleMoves = []
        if (grid[self.pinkyCurrentY - 1][self.pinkyCurrentX]) == 0:
            self.pinkyPossibleMoves.append(
                (self.pinkyCurrentX, self.pinkyCurrentY - 1, "UP")
            )
        if (grid[self.pinkyCurrentY][self.pinkyCurrentX + 1]) == 0:
            self.pinkyPossibleMoves.append(
                (self.pinkyCurrentX + 1, self.pinkyCurrentY, "RIGHT")
            )
        if (grid[self.pinkyCurrentY + 1][self.pinkyCurrentX]) == 0:
            self.pinkyPossibleMoves.append(
                (self.pinkyCurrentX, self.pinkyCurrentY + 1, "DOWN")
            )
        if (grid[self.pinkyCurrentY][self.pinkyCurrentX - 1]) == 0:
            self.pinkyPossibleMoves.append(
                (self.pinkyCurrentX - 1, self.pinkyCurrentY, "LEFT")
            )
        if (grid[self.blinkyCurrentY - 1][self.blinkyCurrentX]) == 0:
            self.blinkyPossibleMoves.append(
                (self.blinkyCurrentX, self.blinkyCurrentY - 1, "UP")
            )
        if (grid[self.blinkyCurrentY][self.blinkyCurrentX + 1]) == 0:
            self.blinkyPossibleMoves.append(
                (self.blinkyCurrentX + 1, self.blinkyCurrentY, "RIGHT")
            )
        if (grid[self.blinkyCurrentY + 1][self.blinkyCurrentX]) == 0:
            self.blinkyPossibleMoves.append(
                (self.blinkyCurrentX, self.blinkyCurrentY + 1, "DOWN")
            )
        if (grid[self.blinkyCurrentY][self.blinkyCurrentX - 1]) == 0:
            self.blinkyPossibleMoves.append(
                (self.blinkyCurrentX - 1, self.blinkyCurrentY, "LEFT")
            )
        if (grid[self.inkyCurrentY - 1][self.inkyCurrentX]) == 0:
            self.inkyPossibleMoves.append(
                (self.inkyCurrentX, self.inkyCurrentY - 1, "UP")
            )
        if (grid[self.inkyCurrentY][self.inkyCurrentX + 1]) == 0:
            self.inkyPossibleMoves.append(
                (self.inkyCurrentX + 1, self.inkyCurrentY, "RIGHT")
            )
        if (grid[self.inkyCurrentY + 1][self.inkyCurrentX]) == 0:
            self.inkyPossibleMoves.append(
                (self.inkyCurrentX, self.inkyCurrentY + 1, "DOWN")
            )
        if (grid[self.inkyCurrentY][self.inkyCurrentX - 1]) == 0:
            self.inkyPossibleMoves.append(
                (self.inkyCurrentX - 1, self.inkyCurrentY, "LEFT")
            )
        if (grid[self.clydeCurrentY - 1][self.clydeCurrentX]) == 0:
            self.clydePossibleMoves.append(
                (self.clydeCurrentX, self.clydeCurrentY - 1, "UP")
            )
        if (grid[self.clydeCurrentY][self.clydeCurrentX + 1]) == 0:
            self.clydePossibleMoves.append(
                (self.clydeCurrentX + 1, self.clydeCurrentY, "RIGHT")
            )
        if (grid[self.clydeCurrentY + 1][self.clydeCurrentX]) == 0:
            self.clydePossibleMoves.append(
                (self.clydeCurrentX, self.clydeCurrentY + 1, "DOWN")
            )
        if (grid[self.clydeCurrentY][self.clydeCurrentX - 1]) == 0:
            self.clydePossibleMoves.append(
                (self.clydeCurrentX - 1, self.clydeCurrentY, "LEFT")
            )

    def setFrightenedMode(self) -> None:
        if self.currentPinkyMode != "EATEN":
            if self.currentPinkyMode != "FRIGHTENED":
                self.previousPinkyCounterValue = self.pinkyCounter
                self.previousPinkyMode = self.currentPinkyMode
            self.currentPinkyMode = "FRIGHTENED"
            self.pinkyCounter = 0
            self.initialize_ghosts("pinky")

        if self.currentBlinkyMode != "EATEN":
            if self.currentBlinkyMode != "FRIGHTENED":
                self.previousBlinkyCounterValue = self.blinkyCounter
                self.previousBlinkyMode = self.currentBlinkyMode
            self.currentBlinkyMode = "FRIGHTENED"
            self.blinkyCounter = 0
            self.initialize_ghosts("blinky")
        if self.currentInkyMode != "EATEN":
            if self.currentInkyMode != "FRIGHTENED":
                self.previousInkyCounterValue = self.inkyCounter
                self.previousInkyMode = self.currentInkyMode
            self.currentInkyMode = "FRIGHTENED"
            self.inkyCounter = 0
            self.initialize_ghosts("inky")
        if self.currentClydeMode != "EATEN":
            if self.currentClydeMode != "FRIGHTENED":
                self.previousClydeCounterValue = self.clydeCounter
                self.previousClydeMode = self.currentClydeMode
            self.currentClydeMode = "FRIGHTENED"
            self.clydeCounter = 0
            self.initialize_ghosts("clyde")

    def updateGhostModesIfNecessary(self) -> None:
        self.pinkyCounter += 1
        if self.pinkyCounter == 116 and self.currentPinkyMode == "SCATTER":
            self.pinkyCounter = 0
            self.currentPinkyMode = "CHASE"
            self.initialize_ghosts("pinky")
        elif self.pinkyCounter == 333 and self.currentPinkyMode == "CHASE":
            self.pinkyCounter = 0
            self.currentPinkyMode = "SCATTER"
            self.initialize_ghosts("pinky")
        elif (
            self.pinkyCounter == 130
            and self.currentPinkyMode == "FRIGHTENED"
        ):
            self.pinkyCounter = self.previousPinkyCounterValue
            self.currentPinkyMode = self.previousPinkyMode
            self.initialize_ghosts("pinky")
        elif self.pinkyCounter == 83 and self.currentPinkyMode == "EATEN":
            self.pinkyCounter = self.previousPinkyCounterValue
            self.currentPinkyMode = self.previousPinkyMode
            self.initialize_ghosts("pinky")
        self.blinkyCounter += 1
        if self.blinkyCounter == 116 and self.currentBlinkyMode == "SCATTER":
            self.blinkyCounter = 0
            self.currentBlinkyMode = "CHASE"
            self.initialize_ghosts("blinky")
        elif self.blinkyCounter == 333 and self.currentBlinkyMode == "CHASE":
            self.blinkyCounter = 0
            self.currentBlinkyMode = "SCATTER"
            self.initialize_ghosts("blinky")
        elif (
            self.blinkyCounter == 130
            and self.currentBlinkyMode == "FRIGHTENED"
        ):
            self.blinkyCounter = \
                self.previousBlinkyCounterValue
            self.currentBlinkyMode = self.previousBlinkyMode
            self.initialize_ghosts("blinky")
        elif self.blinkyCounter == 83 and self.currentBlinkyMode == "EATEN":
            self.blinkyCounter = self.previousBlinkyCounterValue
            self.currentBlinkyMode = self.previousBlinkyMode
            self.initialize_ghosts("blinky")
        self.inkyCounter += 1
        if self.inkyCounter == 116 and self.currentInkyMode == "SCATTER":
            self.inkyCounter = 0
            self.currentInkyMode = "CHASE"
            self.initialize_ghosts("inky")
        elif self.inkyCounter == 333 and self.currentInkyMode == "CHASE":
            self.inkyCounter = 0
            self.currentInkyMode = "SCATTER"
            self.initialize_ghosts("inky")
        elif self.inkyCounter == 130 and self.currentInkyMode == "FRIGHTENED":
            self.inkyCounter = self.previousInkyCounterValue
            self.currentInkyMode = self.previousInkyMode
            self.initialize_ghosts("inky")
        elif self.inkyCounter == 83 and self.currentInkyMode == "EATEN":
            self.inkyCounter = self.previousInkyCounterValue
            self.currentInkyMode = self.previousInkyMode
            self.initialize_ghosts("inky")
        self.clydeCounter += 1
        if self.clydeCounter == 116 and self.currentClydeMode == "SCATTER":
            self.clydeCounter = 0
            self.currentClydeMode = "CHASE"
            self.initialize_ghosts("clyde")
        elif self.clydeCounter == 333 and self.currentClydeMode == "CHASE":
            self.clydeCounter = 0
            self.currentClydeMode = "SCATTER"
            self.initialize_ghosts("clyde")
        elif (
            self.clydeCounter == 130
            and self.currentClydeMode == "FRIGHTENED"
        ):
            self.clydeCounter = self.previousClydeCounterValue
            self.currentClydeMode = self.previousClydeMode
            self.initialize_ghosts("clyde")
        elif self.clydeCounter == 83 and self.currentClydeMode == "EATEN":
            self.clydeCounter = self.previousClydeCounterValue
            self.currentClydeMode = self.previousClydeMode
            self.initialize_ghosts("clyde")

    def initialize_ghosts(self, ghost: str) -> None:
        if ghost == "pinky":
            self.previousPinkyX = -1
            self.previousPinkyY = -1
        elif ghost == "blinky":
            self.previousBlinkyX = -1
            self.previousBlinkyY = -1
        elif ghost == "inky":
            self.previousInkyX = -1
            self.previousInkyY = -1
        elif ghost == "clyde":
            self.previousClydeX = -1
            self.previousClydeY = -1

