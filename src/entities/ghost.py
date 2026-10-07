from typing import Any


class Ghost:
    def __init__(
        self,
        pinkyEntity: Any,
        blinkyEntity: Any,
        inkyEntity: Any,
        clydeEntity: Any
    ) -> None:
        self.pinkyEntity = pinkyEntity
        self.blinkyEntity = blinkyEntity
        self.inkyEntity = inkyEntity
        self.clydeEntity = clydeEntity
        self.pinkyCurrentX = self.pinkyEntity.entityOriginalX
        self.pinkyCurrentY = self.pinkyEntity.entityOriginalY
        self.blinkyCurrentX = self.blinkyEntity.entityOriginalX
        self.blinkyCurrentY = self.blinkyEntity.entityOriginalY
        self.inkyCurrentX = self.inkyEntity.entityOriginalX
        self.inkyCurrentY = self.inkyEntity.entityOriginalY
        self.clydeCurrentX = self.clydeEntity.entityOriginalX
        self.clydeCurrentY = self.clydeEntity.entityOriginalY
        self.pinkyPossibleMoves = []
        self.blinkyPossibleMoves = []
        self.inkyPossibleMoves = []
        self.clydePossibleMoves = []

        self.frightenedCounter = 0

        self.currentPinkyMode = "SCATTER"
        self.currentBlinkyMode = "SCATTER"
        self.currentInkyMode = "SCATTER"
        self.currentClydeMode = "SCATTER"



        self.previousPinkyMode = "None"
        self.previousBlinkyMode = "None"
        self.previousInkyMode = "None"
        self.previousClydeMode = "None"


        self.previousPinkyCounterValue = -1;
        self.previousBlinkyCounterValue = -1;
        self.previousInkyCounterValue = -1;
        self.previousClydeCounterValue = -1;




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

    def prepareGhostsPossibleMoves(self, grid):
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

    def updateGhostModesIfNecessary(self):
        self.pinkyCounter += 1
        if self.pinkyCounter == 116 and self.currentPinkyMode == "SCATTER":
            self.pinkyCounter = 0
            self.currentPinkyMode = "CHASE"
            self.initialize_ghosts("pinky")
        elif self.pinkyCounter == 333 and self.currentPinkyMode == "CHASE":
            self.pinkyCounter = 0
            self.currentPinkyMode = "SCATTER"
            self.initialize_ghosts("pinky")
        elif self.pinkyCounter == 116 and self.currentPinkyMode == "FRIGHTENED":
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
        elif self.blinkyCounter == 116 and self.currentBlinkyMode == "FRIGHTENED":
            self.blinkyCounter = self.previousBlinkyCounterValue
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
        elif self.inkyCounter == 116 and self.currentInkyMode == "FRIGHTENED":
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
        elif self.clydeCounter == 116 and self.currentClydeMode == "FRIGHTENED":
            self.clydeCounter = self.previousClydeCounterValue
            self.currentClydeMode = self.previousClydeMode
            self.initialize_ghosts("clyde")
        elif self.clydeCounter == 83 and self.currentClydeMode == "EATEN":
            self.clydeCounter = self.previousClydeCounterValue
            self.currentClydeMode = self.previousClydeMode
            self.initialize_ghosts("clyde")

    def initialize_ghosts(self, ghost:str):
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

    def runAwayFromPacman(self, ghost: str, goalX, goalY) -> str:
        if self.frightenedCounter % 2 == 0:
            return
        if ghost == "pinky":
            pinkyNewPathCost = float("-inf")
            pinkyWinnerDirection = "None"
            for i in range(len(self.pinkyPossibleMoves)):
                value = (self.pinkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.pinkyPossibleMoves[i][1] - goalY) ** 2
                if self.previousPinkyX == self.pinkyPossibleMoves[i][0]:
                    if self.previousPinkyY == self.pinkyPossibleMoves[i][1]:
                        if (value > 4):
                            continue
                if pinkyNewPathCost < value:
                    pinkyNewPathCost = value
                    pinkyWinnerDirection = self.pinkyPossibleMoves[i][2]
            self.previousPinkyX = self.pinkyCurrentX
            self.previousPinkyY = self.pinkyCurrentY
            if pinkyWinnerDirection == "UP":
                self.pinkyCurrentY -= 1
            elif pinkyWinnerDirection == "RIGHT":
                self.pinkyCurrentX += 1
            elif pinkyWinnerDirection == "LEFT":
                self.pinkyCurrentX -= 1
            elif pinkyWinnerDirection == "DOWN":
                self.pinkyCurrentY += 1
        elif ghost == "blinky":
            blinkyNewPathCost = float("-inf")
            blinkyWinnerDirection = "None"
            for i in range(len(self.blinkyPossibleMoves)):
                value = (self.blinkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.blinkyPossibleMoves[i][1] - goalY) ** 2
                if self.previousBlinkyX == self.blinkyPossibleMoves[i][0]:
                    if self.previousBlinkyY == self.blinkyPossibleMoves[i][1]:
                        if (value > 4):
                            continue
                if blinkyNewPathCost < value:
                    blinkyNewPathCost = value
                    blinkyWinnerDirection = self.blinkyPossibleMoves[i][2]
            self.previousBlinkyX = self.blinkyCurrentX
            self.previousBlinkyY = self.blinkyCurrentY
            if blinkyWinnerDirection == "UP":
                self.blinkyCurrentY -= 1
            elif blinkyWinnerDirection == "RIGHT":
                self.blinkyCurrentX += 1
            elif blinkyWinnerDirection == "LEFT":
                self.blinkyCurrentX -= 1
            elif blinkyWinnerDirection == "DOWN":
                self.blinkyCurrentY += 1
        elif ghost == "inky":
            inkyNewPathCost = float("-inf")
            inkyWinnerDirection = "None"
            for i in range(len(self.inkyPossibleMoves)):
                value = (self.inkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.inkyPossibleMoves[i][1] - goalY) ** 2
                if self.previousInkyX == self.inkyPossibleMoves[i][0]:
                    if self.previousInkyY == self.inkyPossibleMoves[i][1]:
                        if (value > 4):
                            continue
                if inkyNewPathCost < value:
                    inkyNewPathCost = value
                    inkyWinnerDirection = self.inkyPossibleMoves[i][2]
            self.previousInkyX = self.inkyCurrentX
            self.previousInkyY = self.inkyCurrentY
            if inkyWinnerDirection == "UP":
                self.inkyCurrentY -= 1
            elif inkyWinnerDirection == "RIGHT":
                self.inkyCurrentX += 1
            elif inkyWinnerDirection == "LEFT":
                self.inkyCurrentX -= 1
            elif inkyWinnerDirection == "DOWN":
                self.inkyCurrentY += 1
        elif ghost == "clyde":
            clydeNewPathCost = float("-inf")
            clydeWinnerDirection = "None"
            for i in range(len(self.clydePossibleMoves)):
                value = (self.clydePossibleMoves[i][0] - goalX) ** 2
                value += (self.clydePossibleMoves[i][1] - goalY) ** 2
                if self.previousClydeX == self.clydePossibleMoves[i][0]:
                    if self.previousClydeY == self.clydePossibleMoves[i][1]:
                        if (value > 4):
                            continue
                if clydeNewPathCost < value:
                    clydeNewPathCost = value
                    clydeWinnerDirection = self.clydePossibleMoves[i][2]
            self.previousClydeX = self.clydeCurrentX
            self.previousClydeY = self.clydeCurrentY
            if clydeWinnerDirection == "UP":
                self.clydeCurrentY -= 1
            elif clydeWinnerDirection == "RIGHT":
                self.clydeCurrentX += 1
            elif clydeWinnerDirection == "LEFT":
                self.clydeCurrentX -= 1
            elif clydeWinnerDirection == "DOWN":
                self.clydeCurrentY += 1

    def setFrightenedMode(self):
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

    def MoveGhostToTarget(self, ghost: str, goalX, goalY) -> str:
        if ghost == "pinky":
            pinkyNewPathCost = float("inf")
            pinkyWinnerDirection = "None"
            for i in range(len(self.pinkyPossibleMoves)):
                if self.previousPinkyX == self.pinkyPossibleMoves[i][0]:
                    if self.previousPinkyY == self.pinkyPossibleMoves[i][1]:
                        continue
                value = (self.pinkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.pinkyPossibleMoves[i][1] - goalY) ** 2
                if pinkyNewPathCost > value:
                    pinkyNewPathCost = value
                    pinkyWinnerDirection = self.pinkyPossibleMoves[i][2]
            self.previousPinkyX = self.pinkyCurrentX
            self.previousPinkyY = self.pinkyCurrentY
            if pinkyWinnerDirection == "UP":
                self.pinkyCurrentY -= 1
            elif pinkyWinnerDirection == "RIGHT":
                self.pinkyCurrentX += 1
            elif pinkyWinnerDirection == "LEFT":
                self.pinkyCurrentX -= 1
            elif pinkyWinnerDirection == "DOWN":
                self.pinkyCurrentY += 1
        elif ghost == "blinky":
            blinkyNewPathCost = float("inf")
            blinkyWinnerDirection = "None"
            for i in range(len(self.blinkyPossibleMoves)):
                if self.previousBlinkyX == self.blinkyPossibleMoves[i][0]:
                    if self.previousBlinkyY == self.blinkyPossibleMoves[i][1]:
                        continue
                value = (self.blinkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.blinkyPossibleMoves[i][1] - goalY) ** 2
                if blinkyNewPathCost > value:
                    blinkyNewPathCost = value
                    blinkyWinnerDirection = self.blinkyPossibleMoves[i][2]
            self.previousBlinkyX = self.blinkyCurrentX
            self.previousBlinkyY = self.blinkyCurrentY
            if blinkyWinnerDirection == "UP":
                self.blinkyCurrentY -= 1
            elif blinkyWinnerDirection == "RIGHT":
                self.blinkyCurrentX += 1
            elif blinkyWinnerDirection == "LEFT":
                self.blinkyCurrentX -= 1
            elif blinkyWinnerDirection == "DOWN":
                self.blinkyCurrentY += 1
        elif ghost == "inky":
            inkyNewPathCost = float("inf")
            inkyWinnerDirection = "None"
            for i in range(len(self.inkyPossibleMoves)):
                if self.previousInkyX == self.inkyPossibleMoves[i][0]:
                    if self.previousInkyY == self.inkyPossibleMoves[i][1]:
                        continue
                value = (self.inkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.inkyPossibleMoves[i][1] - goalY) ** 2
                if inkyNewPathCost > value:
                    inkyNewPathCost = value
                    inkyWinnerDirection = self.inkyPossibleMoves[i][2]
            self.previousInkyX = self.inkyCurrentX
            self.previousInkyY = self.inkyCurrentY
            if inkyWinnerDirection == "UP":
                self.inkyCurrentY -= 1
            elif inkyWinnerDirection == "RIGHT":
                self.inkyCurrentX += 1
            elif inkyWinnerDirection == "LEFT":
                self.inkyCurrentX -= 1
            elif inkyWinnerDirection == "DOWN":
                self.inkyCurrentY += 1
        elif ghost == "clyde":
            clydeNewPathCost = float("inf")
            clydeWinnerDirection = "None"
            for i in range(len(self.clydePossibleMoves)):
                if self.previousClydeX == self.clydePossibleMoves[i][0]:
                    if self.previousClydeY == self.clydePossibleMoves[i][1]:
                        continue
                value = (self.clydePossibleMoves[i][0] - goalX) ** 2
                value += (self.clydePossibleMoves[i][1] - goalY) ** 2
                if clydeNewPathCost > value:
                    clydeNewPathCost = value
                    clydeWinnerDirection = self.clydePossibleMoves[i][2]
            self.previousClydeX = self.clydeCurrentX
            self.previousClydeY = self.clydeCurrentY
            if clydeWinnerDirection == "UP":
                self.clydeCurrentY -= 1
            elif clydeWinnerDirection == "RIGHT":
                self.clydeCurrentX += 1
            elif clydeWinnerDirection == "LEFT":
                self.clydeCurrentX -= 1
            elif clydeWinnerDirection == "DOWN":
                self.clydeCurrentY += 1