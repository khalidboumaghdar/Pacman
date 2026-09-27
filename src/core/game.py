from typing import Any
import pygame


class Game:
    def __init__(self, width: int, height: int, grid: list[list[int]], player: Any, ghost: Any, pickups: Any) -> None:
        self.width = width
        self.height = height
        self.grid = grid
        self.player = player
        self.ghost = ghost
        self.pickups = pickups
        self.isRunning = True
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.score = 0

    def isDirectionOpen(self, direction) -> bool:
        if direction == "UP":
            if (self.grid[int(self.player.currentY - 1)][int(self.player.currentX)] == 1):
                return False
        elif direction == "RIGHT":
            if (self.grid[int(self.player.currentY)][int(self.player.currentX + 1)] == 1):
                return False
        elif direction == "LEFT":
            if (self.grid[int(self.player.currentY)][int(self.player.currentX - 1)] == 1):
                return False
        elif direction == "DOWN":
            if (self.grid[int(self.player.currentY + 1)][int(self.player.currentX)] == 1):
                return False
        if direction == "None":
            return False
        return True

    def movePacman(self):
        if self.isDirectionOpen(self.player.ignoredDirection) == True:
            self.player.nextDirection = self.player.ignoredDirection
            self.player.ignoredDirection = "None"
        if self.player.nextDirection == "UP":
            if (self.grid[int(self.player.currentY - 1)][int(self.player.currentX)] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentY -= 1
        elif self.player.nextDirection == "RIGHT":
            if (self.grid[int(self.player.currentY)][int(self.player.currentX + 1)] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentX += 1
        elif self.player.nextDirection == "LEFT":
            if (self.grid[int(self.player.currentY)][int(self.player.currentX - 1)] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentX -= 1
        elif self.player.nextDirection == "DOWN":
            if (self.grid[int(self.player.currentY + 1)][int(self.player.currentX)] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentY += 1
        if self.player.nextDirection != self.player.previousDirection:
            self.player.ignoredDirection = "None"

    def pygamePygameStringPut(self, window: Any, x: int, y: int, stringToPutInWindow):
        dddd = pygame.font.Font('freesansbold.ttf', 20)
        text = dddd.render(stringToPutInWindow, True, self.white, self.black)
        text_rect = text.get_rect()
        text_rect.center = (x * 20, y * 20)
        window.blit(text, text_rect)

    def checkIsAGhostEatedPacman(self) -> bool:
        if self.player.currentX == self.ghost.pinkyCurrentX and self.player.currentY == self.ghost.pinkyCurrentY:
            if self.ghost.currentPinkyMode != "FRIGHTENED":
                if self.ghost.currentPinkyMode != "EATEN":
                    return True
        elif self.player.currentX == self.ghost.blinkyCurrentX and self.player.currentY == self.ghost.blinkyCurrentY:
            if self.ghost.currentBlinkyMode != "FRIGHTENED":
                if self.ghost.currentBlinkyMode != "EATEN":
                    return True
        elif self.player.currentX == self.ghost.inkyCurrentX and self.player.currentY == self.ghost.inkyCurrentY:
            if self.ghost.currentInkyMode != "FRIGHTENED":
                if self.ghost.currentInkyMode != "EATEN":
                    return True
        elif self.player.currentX == self.ghost.clydeCurrentX and self.player.currentY == self.ghost.clydeCurrentY:
            if self.ghost.currentClydeMode != "FRIGHTENED":
                if self.ghost.currentClydeMode != "EATEN":
                    return True
        return False

    def checkIsPacmanEatedGhost(self) -> bool:
        if self.player.currentX == self.ghost.pinkyCurrentX and self.player.currentY == self.ghost.pinkyCurrentY:
            if self.ghost.currentPinkyMode == "FRIGHTENED":
                return True
        if self.player.currentX == self.ghost.blinkyCurrentX and self.player.currentY == self.ghost.blinkyCurrentY:
            if self.ghost.currentBlinkyMode == "FRIGHTENED":
                return True
        if self.player.currentX == self.ghost.inkyCurrentX and self.player.currentY == self.ghost.inkyCurrentY:
            if self.ghost.currentInkyMode == "FRIGHTENED":
                return True
        if self.player.currentX == self.ghost.clydeCurrentX and self.player.currentY == self.ghost.clydeCurrentY:
            if self.ghost.currentClydeMode == "FRIGHTENED":
                return True
        return False

    def changeGhostModeToEaten(self):
        if self.player.currentX == self.ghost.pinkyCurrentX and self.player.currentY == self.ghost.pinkyCurrentY:
                self.ghost.currentPinkyMode = "EATEN"
                self.ghost.pinkyCounter = 0
                self.ghost.pinkyCurrentX = self.ghost.pinkyEntity.entityOriginalX
                self.ghost.pinkyCurrentY = self.ghost.pinkyEntity.entityOriginalY
        if self.player.currentX == self.ghost.blinkyCurrentX and self.player.currentY == self.ghost.blinkyCurrentY:
                self.ghost.currentBlinkyMode = "EATEN"
                self.ghost.blinkyCounter = 0
                self.ghost.blinkyCurrentX = self.ghost.blinkyEntity.entityOriginalX
                self.ghost.blinkyCurrentY = self.ghost.blinkyEntity.entityOriginalY
        if self.player.currentX == self.ghost.inkyCurrentX and self.player.currentY == self.ghost.inkyCurrentY:
                self.ghost.currentInkyMode = "EATEN"
                self.ghost.inkyCounter = 0
                self.ghost.inkyCurrentX = self.ghost.inkyEntity.entityOriginalX
                self.ghost.inkyCurrentY = self.ghost.inkyEntity.entityOriginalY
        if self.player.currentX == self.ghost.clydeCurrentX and self.player.currentY == self.ghost.clydeCurrentY:
                self.ghost.currentClydeMode = "EATEN"
                self.ghost.clydeCounter = 0
                self.ghost.clydeCurrentX = self.ghost.clydeEntity.entityOriginalX
                self.ghost.clydeCurrentY = self.ghost.clydeEntity.entityOriginalY

    def displayMap(self, renderer: Any) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if self.pickups.pacgums[y][x] == 50:
                    if self.player.currentX == x and self.player.currentY == y:
                        self.ghost.setFrightenedMode()
                if self.grid[y][x] == 1:
                    self.pygamePygameStringPut(renderer.screen, x, y, "#")
                elif x == self.ghost.pinkyCurrentX and y == self.ghost.pinkyCurrentY:
                    if self.ghost.currentPinkyMode == "EATEN":
                        self.pygamePygameStringPut(renderer.screen, x, y, "@")
                    elif self.ghost.currentPinkyMode == "FRIGHTENED":
                        self.pygamePygameStringPut(renderer.screen, x, y, "1")
                    else:
                        self.pygamePygameStringPut(renderer.screen, x, y, "p")
                elif x == self.ghost.blinkyCurrentX and y == self.ghost.blinkyCurrentY:
                    if self.ghost.currentBlinkyMode == "EATEN":
                        self.pygamePygameStringPut(renderer.screen, x, y, "@")
                    elif self.ghost.currentBlinkyMode == "FRIGHTENED":
                        self.pygamePygameStringPut(renderer.screen, x, y, "2")
                    else:
                        self.pygamePygameStringPut(renderer.screen, x, y, "b")
                elif x == self.ghost.inkyCurrentX and y == self.ghost.inkyCurrentY:
                    if self.ghost.currentInkyMode == "EATEN":
                        self.pygamePygameStringPut(renderer.screen, x, y, "@")
                    elif self.ghost.currentInkyMode == "FRIGHTENED":
                        self.pygamePygameStringPut(renderer.screen, x, y, "3")
                    else:
                        self.pygamePygameStringPut(renderer.screen, x, y, "i")
                elif x == self.ghost.clydeCurrentX and y == self.ghost.clydeCurrentY:
                    if self.ghost.currentClydeMode == "EATEN":
                        self.pygamePygameStringPut(renderer.screen, x, y, "@")
                    elif self.ghost.currentClydeMode == "FRIGHTENED":
                        self.pygamePygameStringPut(renderer.screen, x, y, "4")
                    else:
                        self.pygamePygameStringPut(renderer.screen, x, y, "c")
                elif self.player.currentX == x and self.player.currentY == y:
                    self.pygamePygameStringPut(renderer.screen, x, y, "P")
                    if self.pickups.pacgums[y][x] == 10:
                        self.score += 10
                        self.pickups.pacgums[y][x] = 0
                    elif self.pickups.pacgums[y][x] == 50:
                        self.score += 50
                        self.pickups.pacgums[y][x] = 0
                elif self.pickups.pacgums[y][x] == 10:
                    self.pygamePygameStringPut(renderer.screen, x, y, ".")
                elif self.pickups.pacgums[y][x] == 50:
                    self.pygamePygameStringPut(renderer.screen, x, y, "O")
        self.pygamePygameStringPut(renderer.screen, 0, self.height, f"                     score: {self.score}")

    def updateGhostModesIfNecessary(self):
        self.ghost.pinkyCounter += 1
        if self.ghost.pinkyCounter == 116 and self.ghost.currentPinkyMode == "SCATTER":
            self.ghost.pinkyCounter = 0
            self.ghost.currentPinkyMode = "CHASE"
            self.ghost.initialize_ghosts("pinky")
        elif self.ghost.pinkyCounter == 333 and self.ghost.currentPinkyMode == "CHASE":
            self.ghost.pinkyCounter = 0
            self.ghost.currentPinkyMode = "SCATTER"
            self.ghost.initialize_ghosts("pinky")
        elif self.ghost.pinkyCounter == 116 and self.ghost.currentPinkyMode == "FRIGHTENED":
            self.ghost.pinkyCounter = self.ghost.previousPinkyCounterValue
            self.ghost.currentPinkyMode = self.ghost.previousPinkyMode
            self.ghost.initialize_ghosts("pinky")
        elif self.ghost.pinkyCounter == 83 and self.ghost.currentPinkyMode == "EATEN":
            self.ghost.pinkyCounter = self.ghost.previousPinkyCounterValue
            self.ghost.currentPinkyMode = self.ghost.previousPinkyMode
            self.ghost.initialize_ghosts("pinky")


        self.ghost.blinkyCounter += 1
        if self.ghost.blinkyCounter == 116 and self.ghost.currentBlinkyMode == "SCATTER":
            self.ghost.blinkyCounter = 0
            self.ghost.currentBlinkyMode = "CHASE"
            self.ghost.initialize_ghosts("blinky")
        elif self.ghost.blinkyCounter == 333 and self.ghost.currentBlinkyMode == "CHASE":
            self.ghost.blinkyCounter = 0
            self.ghost.currentBlinkyMode = "SCATTER"
            self.ghost.initialize_ghosts("blinky")
        elif self.ghost.blinkyCounter == 116 and self.ghost.currentBlinkyMode == "FRIGHTENED":
            self.ghost.blinkyCounter = self.ghost.previousBlinkyCounterValue
            self.ghost.currentBlinkyMode = self.ghost.previousBlinkyMode
            self.ghost.initialize_ghosts("blinky")
        elif self.ghost.blinkyCounter == 83 and self.ghost.currentBlinkyMode == "EATEN":
            self.ghost.blinkyCounter = self.ghost.previousBlinkyCounterValue
            self.ghost.currentBlinkyMode = self.ghost.previousBlinkyMode
            self.ghost.initialize_ghosts("blinky")

        self.ghost.inkyCounter += 1
        if self.ghost.inkyCounter == 116 and self.ghost.currentInkyMode == "SCATTER":
            self.ghost.inkyCounter = 0
            self.ghost.currentInkyMode = "CHASE"
            self.ghost.initialize_ghosts("inky")
        elif self.ghost.inkyCounter == 333 and self.ghost.currentInkyMode == "CHASE":
            self.ghost.inkyCounter = 0
            self.ghost.currentInkyMode = "SCATTER"
            self.ghost.initialize_ghosts("inky")
        elif self.ghost.inkyCounter == 116 and self.ghost.currentInkyMode == "FRIGHTENED":
            self.ghost.inkyCounter = self.ghost.previousInkyCounterValue
            self.ghost.currentInkyMode = self.ghost.previousInkyMode
            self.ghost.initialize_ghosts("self.ghost")
        elif self.ghost.inkyCounter == 83 and self.ghost.currentInkyMode == "EATEN":
            self.ghost.inkyCounter = self.ghost.previousInkyCounterValue
            self.ghost.currentInkyMode = self.ghost.previousInkyMode
            self.ghost.initialize_ghosts("self.ghost")

        self.ghost.clydeCounter += 1
        if self.ghost.clydeCounter == 116 and self.ghost.currentClydeMode == "SCATTER":
            self.ghost.clydeCounter = 0
            self.ghost.currentClydeMode = "CHASE"
            self.ghost.initialize_ghosts("clyde")
        elif self.ghost.clydeCounter == 333 and self.ghost.currentClydeMode == "CHASE":
            self.ghost.clydeCounter = 0
            self.ghost.currentClydeMode = "SCATTER"
            self.ghost.initialize_ghosts("clyde")
        elif self.ghost.clydeCounter == 116 and self.ghost.currentClydeMode == "FRIGHTENED":
            self.ghost.clydeCounter = self.ghost.previousClydeCounterValue
            self.ghost.currentClydeMode = self.ghost.previousClydeMode
            self.ghost.initialize_ghosts("clyde")
        elif self.ghost.clydeCounter == 83 and self.ghost.currentClydeMode == "EATEN":
            self.ghost.clydeCounter = self.ghost.previousClydeCounterValue
            self.ghost.currentClydeMode = self.ghost.previousClydeMode
            self.ghost.initialize_ghosts("clyde")

    def moveGhosts(self):
        self.ghost.frightenedCounter += 1
        if self.ghost.currentPinkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget("pinky", 0, 0)
        elif self.ghost.currentPinkyMode == "CHASE":
            self.ghost.MoveGhostToTarget("pinky", self.player.currentX, self.player.currentY)
        elif self.ghost.currentPinkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("pinky", self.player.currentX, self.player.currentY)

        if self.ghost.currentBlinkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget("blinky", self.width - 1, 0)
        elif self.ghost.currentBlinkyMode == "CHASE":
            self.ghost.MoveGhostToTarget("blinky", self.player.currentX, self.player.currentY)
        elif self.ghost.currentBlinkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("blinky", self.player.currentX, self.player.currentY)

        if self.ghost.currentInkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget("inky", 0, self.height - 1)
        elif self.ghost.currentInkyMode == "CHASE":
            self.ghost.MoveGhostToTarget("inky", self.player.currentX, self.player.currentY)
        elif self.ghost.currentInkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("inky", self.player.currentX, self.player.currentY)

        if self.ghost.currentClydeMode == "SCATTER":
            self.ghost.MoveGhostToTarget("clyde", self.width - 1, self.height - 1)
        elif self.ghost.currentClydeMode == "CHASE":
            self.ghost.MoveGhostToTarget("clyde", self.player.currentX, self.player.currentY)
        elif self.ghost.currentClydeMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("clyde", self.player.currentX, self.player.currentY)