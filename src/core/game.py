from typing import Any
import pygame
import sys


class Game:
    def __init__(self, mapWidth: int, mapHeight: int, player: Any, ghost: Any) -> None:
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.player = player
        self.ghost = ghost
        self.isRunning = True
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.score = 0
        self.screen = None
        self.map = None

    def buildGameMap(self, generated_maze) -> None:
        self.map = [[0 for x in range(self.mapWidth)] for y in range(self.mapHeight)]
        for clums in range(len(generated_maze)):
            for rwo in range(len(generated_maze[0])):
                self.map[(clums * 2 + 1) - 1][(rwo * 2 + 1) - 1] = 1
                self.map[(clums * 2 + 1) - 1][(rwo * 2 + 1) + 1] = 1
                self.map[(clums * 2 + 1) + 1][(rwo * 2 + 1) + 1] = 1
                self.map[(clums * 2 + 1) + 1][(rwo * 2 + 1) - 1] = 1
                if generated_maze[clums][rwo]["N"] == 1:
                    self.map[(clums * 2 + 1) - 1][(rwo * 2 + 1)] = 1
                if generated_maze[clums][rwo]["E"] == 1:
                    self.map[(clums * 2 + 1) ][(rwo * 2 + 1) + 1] = 1
                if generated_maze[clums][rwo]["S"] == 1:
                    self.map[(clums * 2 + 1) + 1][(rwo * 2 + 1)] = 1
                if generated_maze[clums][rwo]["W"] == 1:
                    self.map[(clums * 2 + 1) ][(rwo * 2 + 1) - 1] = 1
                if generated_maze[clums][rwo]["N"] == 1:
                    if generated_maze[clums][rwo]["E"] == 1:
                        if generated_maze[clums][rwo]["S"] == 1:
                            if generated_maze[clums][rwo]["W"] == 1:
                                self.map[(clums * 2 + 1) ][(rwo * 2 + 1)] = 1

    def runGameWindow(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.mapWidth * 21, self.mapHeight * 21))
        pygame.display.set_caption("pacman")

    def detectKeyboardInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player.nextDirection = "DOWN"
                if event.key == pygame.K_UP:
                    self.player.nextDirection = "UP"
                if event.key == pygame.K_RIGHT:
                    self.player.nextDirection = "RIGHT"
                if event.key == pygame.K_LEFT:
                    self.player.nextDirection = "LEFT"

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

    def isDirectionOpen(self, direction) -> bool:
        if direction == "UP":
            if (self.map[int(self.player.currentY - 1)][int(self.player.currentX)] == 1):
                return False
        elif direction == "RIGHT":
            if (self.map[int(self.player.currentY)][int(self.player.currentX + 1)] == 1):
                return False
        elif direction == "LEFT":
            if (self.map[int(self.player.currentY)][int(self.player.currentX - 1)] == 1):
                return False
        elif direction == "DOWN":
            if (self.map[int(self.player.currentY + 1)][int(self.player.currentX)] == 1):
                return False
        if direction == "None":
            return False
        return True

    def miniIntialize(self):
        self.player.currentX = self.player.entity.entityOriginalX
        self.player.currentY = self.player.entity.entityOriginalY
        self.player.nextDirection = "None"
        self.player.previousDirection = "None"
        self.player.ignoredDirection = "None"

        self.ghost.pinkyCurrentX = self.ghost.pinkyEntity.entityOriginalX
        self.ghost.pinkyCurrentY = self.ghost.pinkyEntity.entityOriginalY

        self.ghost.blinkyCurrentX = self.ghost.blinkyEntity.entityOriginalX
        self.ghost.blinkyCurrentY = self.ghost.blinkyEntity.entityOriginalY

        self.ghost.inkyCurrentX = self.ghost.inkyEntity.entityOriginalX
        self.ghost.inkyCurrentY = self.ghost.inkyEntity.entityOriginalY

        self.ghost.clydeCurrentX = self.ghost.clydeEntity.entityOriginalX
        self.ghost.clydeCurrentY = self.ghost.clydeEntity.entityOriginalY

        self.ghost.currentPinkyMode = "SCATTER"
        self.ghost.pinkyCounter = 0

        self.ghost.currentBlinkyMode = "SCATTER"
        self.ghost.blinkyCounter = 0

        self.ghost.currentInkyMode = "SCATTER"
        self.ghost.inkyCounter = 0

        self.ghost.currentClydeMode = "SCATTER"
        self.ghost.clydeCounter = 0

    def movePacman(self):
        if self.isDirectionOpen(self.player.ignoredDirection) == True:
            self.player.nextDirection = self.player.ignoredDirection
            self.player.ignoredDirection = "None"
        if self.player.nextDirection == "UP":
            if (self.map[int(self.player.currentY - 1)][int(self.player.currentX)] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentY -= 1
        elif self.player.nextDirection == "RIGHT":
            if (self.map[int(self.player.currentY)][int(self.player.currentX + 1)] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentX += 1
        elif self.player.nextDirection == "LEFT":
            if (self.map[int(self.player.currentY)][int(self.player.currentX - 1)] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentX -= 1
        elif self.player.nextDirection == "DOWN":
            if (self.map[int(self.player.currentY + 1)][int(self.player.currentX)] == 1):
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

    def moveGhosts(self):
        self.ghost.frightenedCounter += 1
        if self.ghost.currentPinkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget("pinky", 0, 0)
        elif self.ghost.currentPinkyMode == "CHASE":
            self.ghost.MoveGhostToTarget("pinky", self.player.currentX, self.player.currentY)
        elif self.ghost.currentPinkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("pinky", self.player.currentX, self.player.currentY)

        if self.ghost.currentBlinkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget("blinky", self.mapWidth - 1, 0)
        elif self.ghost.currentBlinkyMode == "CHASE":
            self.ghost.MoveGhostToTarget("blinky", self.player.currentX, self.player.currentY)
        elif self.ghost.currentBlinkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("blinky", self.player.currentX, self.player.currentY)

        if self.ghost.currentInkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget("inky", 0, self.mapHeight - 1)
        elif self.ghost.currentInkyMode == "CHASE":
            self.ghost.MoveGhostToTarget("inky", self.player.currentX, self.player.currentY)
        elif self.ghost.currentInkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("inky", self.player.currentX, self.player.currentY)

        if self.ghost.currentClydeMode == "SCATTER":
            self.ghost.MoveGhostToTarget("clyde", self.mapWidth - 1, self.mapHeight - 1)
        elif self.ghost.currentClydeMode == "CHASE":
            self.ghost.MoveGhostToTarget("clyde", self.player.currentX, self.player.currentY)
        elif self.ghost.currentClydeMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman("clyde", self.player.currentX, self.player.currentY)

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

    def displayMap(self, pickups) -> None:
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                if self.map[y][x] == 1:
                    self.pygamePygameStringPut(self.screen, x, y, "#")
                elif x == self.ghost.pinkyCurrentX and y == self.ghost.pinkyCurrentY:
                    if self.ghost.currentPinkyMode == "EATEN":
                        self.pygamePygameStringPut(self.screen, x, y, "@")
                    elif self.ghost.currentPinkyMode == "FRIGHTENED":
                        self.pygamePygameStringPut(self.screen, x, y, "1")
                    else:
                        self.pygamePygameStringPut(self.screen, x, y, "p")
                elif x == self.ghost.blinkyCurrentX and y == self.ghost.blinkyCurrentY:
                    if self.ghost.currentBlinkyMode == "EATEN":
                        self.pygamePygameStringPut(self.screen, x, y, "@")
                    elif self.ghost.currentBlinkyMode == "FRIGHTENED":
                        self.pygamePygameStringPut(self.screen, x, y, "2")
                    else:
                        self.pygamePygameStringPut(self.screen, x, y, "b")
                elif x == self.ghost.inkyCurrentX and y == self.ghost.inkyCurrentY:
                    if self.ghost.currentInkyMode == "EATEN":
                        self.pygamePygameStringPut(self.screen, x, y, "@")
                    elif self.ghost.currentInkyMode == "FRIGHTENED":
                        self.pygamePygameStringPut(self.screen, x, y, "3")
                    else:
                        self.pygamePygameStringPut(self.screen, x, y, "i")
                elif x == self.ghost.clydeCurrentX and y == self.ghost.clydeCurrentY:
                    if self.ghost.currentClydeMode == "EATEN":
                        self.pygamePygameStringPut(self.screen, x, y, "@")
                    elif self.ghost.currentClydeMode == "FRIGHTENED":
                        self.pygamePygameStringPut(self.screen, x, y, "4")
                    else:
                        self.pygamePygameStringPut(self.screen, x, y, "c")
                elif self.player.currentX == x and self.player.currentY == y:
                    self.pygamePygameStringPut(self.screen, x, y, "P")
                    if pickups.pacgums[y][x] == 10:
                        self.score += 10
                        pickups.pacgums[y][x] = 0
                    elif pickups.pacgums[y][x] == 50:
                        self.score += 50
                        pickups.pacgums[y][x] = 0
                        self.ghost.setFrightenedMode()
                elif pickups.pacgums[y][x] == 10:
                    self.pygamePygameStringPut(self.screen, x, y, ".")
                elif pickups.pacgums[y][x] == 50:
                    self.pygamePygameStringPut(self.screen, x, y, "O")
        self.pygamePygameStringPut(self.screen, 0, self.mapHeight, f"                     score: {self.score}")
        self.pygamePygameStringPut(self.screen, 15, self.mapHeight, f" level: {self.player.currentLevel + 1}/{self.player.allLevels}")
        self.pygamePygameStringPut(self.screen, 30, self.mapHeight, f" lives: {self.player.lives}")