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
        self.currentMode = "SCATTER"
        self.previous_pinky_x = -1
        self.previous_pinky_y = -1
        self.previous_blinky_x = -1
        self.previous_blinky_y = -1
        self.previous_inky_x = -1
        self.previous_inky_y = -1
        self.previous_clyde_x = -1
        self.previous_clyde_y = -1


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

    def MoveGhostToTarget(self, ghost: str, goalX, goalY) -> str:
        if ghost == "pinky":
            pinkyNewPathCost = float("inf")
            pinkyWinnerDirection = "None"
            for i in range(len(self.pinkyPossibleMoves)):
                if self.previous_pinky_x == self.pinkyPossibleMoves[i][0]:
                    if self.previous_pinky_y == self.pinkyPossibleMoves[i][1]:
                        continue
                value = (self.pinkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.pinkyPossibleMoves[i][1] - goalY) ** 2
                if pinkyNewPathCost > value:
                    pinkyNewPathCost = value
                    pinkyWinnerDirection = self.pinkyPossibleMoves[i][2]
            self.previous_pinky_x = self.pinkyCurrentX
            self.previous_pinky_y = self.pinkyCurrentY
            if pinkyWinnerDirection == "UP":
                self.pinkyCurrentY -= 1
            elif pinkyWinnerDirection == "RIGHT":
                self.pinkyCurrentX += 1
            elif pinkyWinnerDirection == "LEFT":
                self.pinkyCurrentX -= 1
            elif pinkyWinnerDirection == "DOWN":
                self.pinkyCurrentY += 1
        elif ghost == "blinky":
            previous_blinky_x = -1
            previous_blinky_y = -1
            blinkyNewPathCost = float("inf")
            blinkyWinnerDirection = "None"
            for i in range(len(self.blinkyPossibleMoves)):
                if self.previous_blinky_x == self.blinkyPossibleMoves[i][0]:
                    if self.previous_blinky_y == self.blinkyPossibleMoves[i][1]:
                        continue
                value = (self.blinkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.blinkyPossibleMoves[i][1] - goalY) ** 2
                if blinkyNewPathCost > value:
                    blinkyNewPathCost = value
                    blinkyWinnerDirection = self.blinkyPossibleMoves[i][2]
            self.previous_blinky_x = self.blinkyCurrentX
            self.previous_blinky_y = self.blinkyCurrentY
            if blinkyWinnerDirection == "UP":
                self.blinkyCurrentY -= 1
            elif blinkyWinnerDirection == "RIGHT":
                self.blinkyCurrentX += 1
            elif blinkyWinnerDirection == "LEFT":
                self.blinkyCurrentX -= 1
            elif blinkyWinnerDirection == "DOWN":
                self.blinkyCurrentY += 1
        elif ghost == "inky":
            previous_inky_x = -1
            previous_inky_y = -1
            inkyNewPathCost = float("inf")
            inkyWinnerDirection = "None"
            for i in range(len(self.inkyPossibleMoves)):
                if self.previous_inky_x == self.inkyPossibleMoves[i][0]:
                    if self.previous_inky_y == self.inkyPossibleMoves[i][1]:
                        continue
                value = (self.inkyPossibleMoves[i][0] - goalX) ** 2
                value += (self.inkyPossibleMoves[i][1] - goalY) ** 2
                if inkyNewPathCost > value:
                    inkyNewPathCost = value
                    inkyWinnerDirection = self.inkyPossibleMoves[i][2]
            self.previous_inky_x = self.inkyCurrentX
            self.previous_inky_y = self.inkyCurrentY
            if inkyWinnerDirection == "UP":
                self.inkyCurrentY -= 1
            elif inkyWinnerDirection == "RIGHT":
                self.inkyCurrentX += 1
            elif inkyWinnerDirection == "LEFT":
                self.inkyCurrentX -= 1
            elif inkyWinnerDirection == "DOWN":
                self.inkyCurrentY += 1
        elif ghost == "clyde":
            previous_clyde_x = -1
            previous_clyde_y = -1
            clydeNewPathCost = float("inf")
            clydeWinnerDirection = "None"
            for i in range(len(self.clydePossibleMoves)):
                if self.previous_clyde_x == self.clydePossibleMoves[i][0]:
                    if self.previous_clyde_y == self.clydePossibleMoves[i][1]:
                        continue
                value = (self.clydePossibleMoves[i][0] - goalX) ** 2
                value += (self.clydePossibleMoves[i][1] - goalY) ** 2
                if clydeNewPathCost > value:
                    clydeNewPathCost = value
                    clydeWinnerDirection = self.clydePossibleMoves[i][2]
            self.previous_clyde_x = self.clydeCurrentX
            self.previous_clyde_y = self.clydeCurrentY
            if clydeWinnerDirection == "UP":
                self.clydeCurrentY -= 1
            elif clydeWinnerDirection == "RIGHT":
                self.clydeCurrentX += 1
            elif clydeWinnerDirection == "LEFT":
                self.clydeCurrentX -= 1
            elif clydeWinnerDirection == "DOWN":
                self.clydeCurrentY += 1