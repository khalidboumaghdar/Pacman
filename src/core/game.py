from typing import Any
import pygame
import sys
from src.core.cheats import Cheat
import os


class Game:
    def __init__(self, mapWidth: int, mapHeight: int, player: Any, ghost: Any, specialData) -> None:
        pygame.init()
        self.c = Cheat(False)
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.player = player
        self.ghost = ghost
        self.isRunning = True
        self.white = (255, 255, 255)
        self.screen = None
        self.font = pygame.font.Font(None, 20)
        self.map = None
        self.wall42 = []
        self.specialData = specialData
        self.isPaused = False

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
                                self.wall42.append(
                                    (str(clums * 2 + 1) + "y", str(rwo * 2 + 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1 - 1) + "y", str(rwo * 2 + 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1) + "y", str(rwo * 2 + 1 + 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1 + 1) + "y", str(rwo * 2 + 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1) + "y", str(rwo * 2 + 1 - 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1 - 1) + "y", str(rwo * 2 + 1 + 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1 + 1) + "y", str(rwo * 2 + 1 + 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1 + 1) + "y", str(rwo * 2 + 1 - 1) + "x")
                                )
                                self.wall42.append(
                                    (str(clums * 2 + 1 - 1) + "y", str(rwo * 2 + 1 - 1) + "x")
                                )
        if self.map[self.player.currentY][self.player.currentX] == 1:
            if self.map[self.player.currentY][self.player.currentX - 1] == 0:
                self.player.currentX -= 1
                self.player.entity.entityOriginalX -= 1
            elif self.map[self.player.currentY][self.player.currentX + 1] == 0:
                self.player.currentX += 1
                self.player.entity.entityOriginalX += 1
            elif self.map[self.player.currentY + 1][self.player.currentX] == 0:
                self.player.currentY += 1
                self.player.entity.entityOriginalY += 1
            elif self.map[self.player.currentY - 1][self.player.currentX] == 0:
                self.player.currentY -= 1
                self.player.entity.entityOriginalY -= 1

    def runGameWindow(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode((self.mapWidth * 21, self.mapHeight * 21), pygame.NOFRAME)

    def detectKeyboardInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    if self.c.check == False:
                        self.c.check = True
                    else:
                        self.c.check = False
                        break
                if event.key == pygame.K_DOWN:
                    self.player.nextDirection = "DOWN"
                if event.key == pygame.K_UP:
                    self.player.nextDirection = "UP"
                if event.key == pygame.K_RIGHT:
                    self.player.nextDirection = "RIGHT"
                if event.key == pygame.K_LEFT:
                    self.player.nextDirection = "LEFT"
                if event.key == pygame.K_p:
                    # print("run menu")
                    self.isPaused = True
                    break

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

    def pygamePygameImagePut(self, window: Any, x: int, y: int, imagesToPutInWindow: str):
        image = pygame.image.load(imagesToPutInWindow)
        window.blit(image, (x * 20, y * 20))

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

    def pygamePygameStringPut(self, window: Any, x: int, y: int, stringToPutInWindow):
        text = self.font.render(stringToPutInWindow, True, self.white)
        window.blit(text, (x * 20, y * 20))


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
                    if ((str(y) + "y", str(x) + "x")) in self.wall42:
                        self.pygamePygameImagePut(self.screen, x, y, "images/wall42.png")
                    else:
                        if (x > 0 and self.map[y][x - 1] == 1):
                            self.pygamePygameImagePut(self.screen, x, y, "images/wall.png")
                        elif (x < self.mapWidth - 1 and self.map[y][x + 1] == 1):
                            self.pygamePygameImagePut(self.screen, x, y, "images/wall.png")
                        else:
                            self.pygamePygameImagePut(self.screen, x, y, "images/wall.png")
                elif x == self.ghost.pinkyCurrentX and y == self.ghost.pinkyCurrentY:
                    if self.ghost.currentPinkyMode == "EATEN":
                        self.pygamePygameImagePut(self.screen, x, y, "images/eaten.png")
                    elif self.ghost.currentPinkyMode == "FRIGHTENED":
                        self.pygamePygameImagePut(self.screen, x, y, "images/Frightened.png")
                    else:
                        self.pygamePygameImagePut(self.screen, x, y, "images/pinky.png")
                elif x == self.ghost.blinkyCurrentX and y == self.ghost.blinkyCurrentY:
                    if self.ghost.currentBlinkyMode == "EATEN":
                        self.pygamePygameImagePut(self.screen, x, y, "images/eaten.png")
                    elif self.ghost.currentBlinkyMode == "FRIGHTENED":
                        self.pygamePygameImagePut(self.screen, x, y, "images/Frightened.png")
                    else:
                        self.pygamePygameImagePut(self.screen, x, y, "images/blinky.png")
                elif x == self.ghost.inkyCurrentX and y == self.ghost.inkyCurrentY:
                    if self.ghost.currentInkyMode == "EATEN":
                        self.pygamePygameImagePut(self.screen, x, y, "images/eaten.png")
                    elif self.ghost.currentInkyMode == "FRIGHTENED":
                        self.pygamePygameImagePut(self.screen, x, y, "images/Frightened.png")
                    else:
                        self.pygamePygameImagePut(self.screen, x, y, "images/inky.png")
                elif x == self.ghost.clydeCurrentX and y == self.ghost.clydeCurrentY:
                    if self.ghost.currentClydeMode == "EATEN":
                        self.pygamePygameImagePut(self.screen, x, y, "images/eaten.png")
                    elif self.ghost.currentClydeMode == "FRIGHTENED":
                        self.pygamePygameImagePut(self.screen, x, y, "images/Frightened.png")
                    else:
                        self.pygamePygameImagePut(self.screen, x, y, "images/clyde.png")
                elif self.player.currentX == x and self.player.currentY == y:
                    if self.player.nextDirection == "UP":
                        self.pygamePygameImagePut(self.screen, x, y, "images/pacmantop.png")
                    elif self.player.nextDirection == "RIGHT":
                        self.pygamePygameImagePut(self.screen, x, y, "images/pacmanright.png")
                    elif self.player.nextDirection == "LEFT":
                        self.pygamePygameImagePut(self.screen, x, y, "images/pacmanleft.png")
                    else:
                        self.pygamePygameImagePut(self.screen, x, y, "images/pacmanbottom.png")
                    if pickups.pacgums[y][x] == 10:
                        self.specialData.score += 10
                        pickups.pacgums[y][x] = 0
                    elif pickups.pacgums[y][x] == 50:
                        self.specialData.score += 50
                        pickups.pacgums[y][x] = 0
                        self.ghost.setFrightenedMode()
                elif pickups.pacgums[y][x] == 10:
                    self.pygamePygameImagePut(self.screen, x, y, "images/smallpickups.png")
                elif pickups.pacgums[y][x] == 50:
                    self.pygamePygameImagePut(self.screen, x, y, "images/bigpickups.png")
        self.pygamePygameStringPut(self.screen, 0, self.mapHeight, f"                     score: {self.specialData.score}")
        self.pygamePygameStringPut(self.screen, 9, self.mapHeight, f" level: {self.specialData.currentLevel + 1}/{self.specialData.allLevels}")
        self.pygamePygameStringPut(self.screen, 15, self.mapHeight, f" lives: {self.specialData.lives}")