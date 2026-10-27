from src.entities.entity import Entity


class Ghost:
    """the class that control the four ghosts properties"""
    def __init__(
        self,
        pinkyEntity: Entity,
        blinkyEntity: Entity,
        inkyEntity: Entity,
        clydeEntity: Entity
    ) -> None:
        """constructor method"""
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
        """prepare right directions that ghosts may move to"""
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
        """ set the frightend mode when pacman eat super-pacgums"""
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

    def initialize_ghosts(self, ghost: str) -> None:
        """intialize or remove ghosts
        previous moves in custom data-base"""
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
