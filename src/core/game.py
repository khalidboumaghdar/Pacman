from typing import Any
import pygame
import sys
from src.core.cheats import Cheat
import os
import time
from src.core.clock import Clock
from src.entities.player import Player
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
from src.entities.specialData import SpecialData


class Game:
    def __init__(
        self,
        clock: Clock,
        mapWidth: int,
        mapHeight: int,
        player: Player,
        ghost: Ghost,
        specialData: SpecialData
    ) -> None:
        pygame.init()
        self.c = Cheat(False)
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.player = player
        self.ghost = ghost
        self.isRunning = True
        self.skyBlue = (135, 206, 235)
        self.screen: Any = None
        self.font = pygame.font.Font(None, 20)
        self.map: list
        self.clock = clock
        self.wall42: list = []
        self.specialData = specialData
        self.isPaused = False

    def buildGameMap(self, generated_maze: list[list]) -> None:
        self.map = [
            [0 for x in range(self.mapWidth)] for y in range(self.mapHeight)
        ]
        for clums in range(len(generated_maze)):
            for rwo in range(len(generated_maze[0])):
                self.map[(clums * 2 + 1) - 1][(rwo * 2 + 1) - 1] = 1
                self.map[(clums * 2 + 1) - 1][(rwo * 2 + 1) + 1] = 1
                self.map[(clums * 2 + 1) + 1][(rwo * 2 + 1) + 1] = 1
                self.map[(clums * 2 + 1) + 1][(rwo * 2 + 1) - 1] = 1
                if generated_maze[clums][rwo]["N"] == 1:
                    self.map[(clums * 2 + 1) - 1][(rwo * 2 + 1)] = 1
                if generated_maze[clums][rwo]["E"] == 1:
                    self.map[(clums * 2 + 1)][(rwo * 2 + 1) + 1] = 1
                if generated_maze[clums][rwo]["S"] == 1:
                    self.map[(clums * 2 + 1) + 1][(rwo * 2 + 1)] = 1
                if generated_maze[clums][rwo]["W"] == 1:
                    self.map[(clums * 2 + 1)][(rwo * 2 + 1) - 1] = 1
                if generated_maze[clums][rwo]["N"] == 1:
                    if generated_maze[clums][rwo]["E"] == 1:
                        if generated_maze[clums][rwo]["S"] == 1:
                            if generated_maze[clums][rwo]["W"] == 1:
                                self.map[(clums * 2 + 1)][(rwo * 2 + 1)] = 1
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1) + "y",
                                        str(rwo * 2 + 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1 - 1) + "y",
                                        str(rwo * 2 + 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1) + "y",
                                        str(rwo * 2 + 1 + 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1 + 1) + "y",
                                        str(rwo * 2 + 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1) + "y",
                                        str(rwo * 2 + 1 - 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1 - 1) + "y",
                                        str(rwo * 2 + 1 + 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1 + 1) + "y",
                                        str(rwo * 2 + 1 + 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1 + 1) + "y",
                                        str(rwo * 2 + 1 - 1) + "x"
                                    )
                                )
                                self.wall42.append(
                                    (
                                        str(clums * 2 + 1 - 1) + "y",
                                        str(rwo * 2 + 1 - 1) + "x"
                                    )
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

    def runGameWindow(self) -> None:
        try:
            os.environ['SDL_VIDEO_CENTERED'] = '1'
            pygame.init()
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        except Exception as e:
            print(e)

    def detectKeyboardInput(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if self.isPaused is True:
                self.isPaused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    if self.c.check is False:
                        self.c.check = True
                        print("Activated Cheat mode!")
                    else:
                        self.c.check = False
                        print("Desactivate cheat mode !")
                    break
                if event.key == pygame.K_F6:
                    if (
                        self.clock.pauseMenu is False
                        and self.clock.pauseTimeCheateMode is False
                    ):
                        self.clock.pauseTimeCheateMode = True
                        self.clock.pauseTime = time.time()
                        print("Activated Cheat mode!")
                    elif self.clock.pauseMenu is False:
                        missingTime = time.time() - self.clock.pauseTime
                        self.clock.oldTime += missingTime
                        self.clock.pauseTimeCheateMode = False
                        print("Desactivate cheat mode !")
                    break
                if event.key == pygame.K_DOWN:
                    self.player.nextDirection = "DOWN"
                    break
                if event.key == pygame.K_UP:
                    self.player.nextDirection = "UP"
                if event.key == pygame.K_RIGHT:
                    self.player.nextDirection = "RIGHT"
                    break
                if event.key == pygame.K_LEFT:
                    self.player.nextDirection = "LEFT"
                    break
                if event.key == pygame.K_p:
                    # print("run menu")
                    if self.isPaused is False:
                        if self.clock.pauseMenu is False:
                            if self.clock.pauseTimeCheateMode is False:
                                self.clock.pauseMenu = True
                                self.clock.pauseTime = time.time()
                                print("Activated pause menu!")
                    self.isPaused = True
                    break

    def changeGhostModeToEaten(self) -> None:
        if self.player.currentX == self.ghost.pinkyCurrentX:
            if self.player.currentY == self.ghost.pinkyCurrentY:
                self.ghost.currentPinkyMode = "EATEN"
                self.ghost.pinkyCounter = 0
                original_x = self.ghost.pinkyEntity.entityOriginalX
                self.ghost.pinkyCurrentX = original_x
                original_y = self.ghost.pinkyEntity.entityOriginalY
                self.ghost.pinkyCurrentY = original_y
        if self.player.currentX == self.ghost.blinkyCurrentX:
            if self.player.currentY == self.ghost.blinkyCurrentY:
                self.ghost.currentBlinkyMode = "EATEN"
                self.ghost.blinkyCounter = 0
                original_x = self.ghost.blinkyEntity.entityOriginalX
                self.ghost.blinkyCurrentX = original_x
                original_y = self.ghost.blinkyEntity.entityOriginalY
                self.ghost.blinkyCurrentY = original_y
        if self.player.currentX == self.ghost.inkyCurrentX:
            if self.player.currentY == self.ghost.inkyCurrentY:
                self.ghost.currentInkyMode = "EATEN"
                self.ghost.inkyCounter = 0
                original_x = self.ghost.inkyEntity.entityOriginalX
                self.ghost.inkyCurrentX = original_x
                original_y = self.ghost.inkyEntity.entityOriginalY
                self.ghost.inkyCurrentY = original_y
        if self.player.currentX == self.ghost.clydeCurrentX:
            if self.player.currentY == self.ghost.clydeCurrentY:
                self.ghost.currentClydeMode = "EATEN"
                self.ghost.clydeCounter = 0
                original_x = self.ghost.clydeEntity.entityOriginalX
                self.ghost.clydeCurrentX = original_x
                original_y = self.ghost.clydeEntity.entityOriginalY
                self.ghost.clydeCurrentY = original_y

    def isDirectionOpen(self, direction: str) -> bool:
        if direction == "UP":
            y = int(self.player.currentY - 1)
            x = int(self.player.currentX)
            if (self.map[y][x] == 1):
                return False
        elif direction == "RIGHT":
            y = int(self.player.currentY)
            x = int(self.player.currentX + 1)
            if (self.map[y][x] == 1):
                return False
        elif direction == "LEFT":
            y = int(self.player.currentY)
            x = int(self.player.currentX - 1)
            if (self.map[y][x] == 1):
                return False
        elif direction == "DOWN":
            y = int(self.player.currentY + 1)
            x = int(self.player.currentX)
            if (self.map[y][x] == 1):
                return False
        if direction == "None":
            return False
        return True

    def miniIntialize(self) -> None:
        time.sleep(0.4)
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

    def movePacman(self) -> None:
        if self.isDirectionOpen(self.player.ignoredDirection) is True:
            self.player.nextDirection = self.player.ignoredDirection
            self.player.ignoredDirection = "None"
        if self.player.nextDirection == "UP":
            y = int(self.player.currentY - 1)
            x = int(self.player.currentX)
            if (self.map[y][x] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentY -= 1
        elif self.player.nextDirection == "RIGHT":
            y = int(self.player.currentY)
            x = int(self.player.currentX + 1)
            if (self.map[y][x] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentX += 1
        elif self.player.nextDirection == "LEFT":
            y = int(self.player.currentY)
            x = int(self.player.currentX - 1)
            if (self.map[y][x] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentX -= 1
        elif self.player.nextDirection == "DOWN":
            y = int(self.player.currentY + 1)
            x = int(self.player.currentX)
            if (self.map[y][x] == 1):
                if self.player.nextDirection != self.player.previousDirection:
                    self.player.ignoredDirection = self.player.nextDirection
                    self.player.nextDirection = self.player.previousDirection
                    self.movePacman()
                return
            self.player.currentY += 1
        if self.player.nextDirection != self.player.previousDirection:
            self.player.ignoredDirection = "None"

    def putImage(self, window: Any, x: int, y: int, image: str) -> None:
        myImage = pygame.image.load(image)
        x = int((x + ((95 - self.mapWidth) / 2)) * 20)
        y = int((y + ((53 - self.mapHeight) / 2)) * 20)
        window.blit(myImage, (x, y))

    def checkIsPacmanEatedGhost(self) -> bool:
        if self.player.currentX == self.ghost.pinkyCurrentX:
            if self.player.currentY == self.ghost.pinkyCurrentY:
                if self.ghost.currentPinkyMode == "FRIGHTENED":
                    return True
        if self.player.currentX == self.ghost.blinkyCurrentX:
            if self.player.currentY == self.ghost.blinkyCurrentY:
                if self.ghost.currentBlinkyMode == "FRIGHTENED":
                    return True
        if self.player.currentX == self.ghost.inkyCurrentX:
            if self.player.currentY == self.ghost.inkyCurrentY:
                if self.ghost.currentInkyMode == "FRIGHTENED":
                    return True
        if self.player.currentX == self.ghost.clydeCurrentX:
            if self.player.currentY == self.ghost.clydeCurrentY:
                if self.ghost.currentClydeMode == "FRIGHTENED":
                    return True
        return False

    def putString(self, window: Any, x: float, y: float, string: str) -> None:
        text = self.font.render(string, True, self.skyBlue)
        window.blit(text, (x * 20, y * 20))

    def moveGhosts(self) -> None:
        self.ghost.frightenedCounter += 1
        if self.ghost.currentPinkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget("pinky", 0, 0)
        elif self.ghost.currentPinkyMode == "CHASE":
            self.ghost.MoveGhostToTarget(
                "pinky",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentPinkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman(
                "pinky",
                self.player.currentX,
                self.player.currentY
            )
        if self.ghost.currentBlinkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget(
                "blinky",
                self.mapWidth - 1,
                0
            )
        elif self.ghost.currentBlinkyMode == "CHASE":
            self.ghost.MoveGhostToTarget(
                "blinky",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentBlinkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman(
                "blinky",
                self.player.currentX,
                self.player.currentY
            )
        if self.ghost.currentInkyMode == "SCATTER":
            self.ghost.MoveGhostToTarget(
                "inky",
                0,
                self.mapHeight - 1
            )
        elif self.ghost.currentInkyMode == "CHASE":
            self.ghost.MoveGhostToTarget(
                "inky",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentInkyMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman(
                "inky",
                self.player.currentX,
                self.player.currentY
            )
        if self.ghost.currentClydeMode == "SCATTER":
            self.ghost.MoveGhostToTarget(
                "clyde",
                self.mapWidth - 1,
                self.mapHeight - 1
            )
        elif self.ghost.currentClydeMode == "CHASE":
            self.ghost.MoveGhostToTarget(
                "clyde",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentClydeMode == "FRIGHTENED":
            self.ghost.runAwayFromPacman(
                "clyde",
                self.player.currentX,
                self.player.currentY
            )

    def checkIsAGhostEatedPacman(self) -> bool:
        player = self.player
        ghost = self.ghost
        if (
            player.currentX == ghost.pinkyCurrentX
            and player.currentY == ghost.pinkyCurrentY
        ):
            if self.ghost.currentPinkyMode != "FRIGHTENED":
                if self.ghost.currentPinkyMode != "EATEN":
                    return True
        elif (
              self.player.currentX == self.ghost.blinkyCurrentX
              and self.player.currentY == self.ghost.blinkyCurrentY
        ):
            if self.ghost.currentBlinkyMode != "FRIGHTENED":
                if self.ghost.currentBlinkyMode != "EATEN":
                    return True
        elif (
              self.player.currentX == self.ghost.inkyCurrentX
              and self.player.currentY == self.ghost.inkyCurrentY
        ):
            if self.ghost.currentInkyMode != "FRIGHTENED":
                if self.ghost.currentInkyMode != "EATEN":
                    return True
        elif (
              self.player.currentX == self.ghost.clydeCurrentX
              and self.player.currentY == self.ghost.clydeCurrentY
        ):
            if self.ghost.currentClydeMode != "FRIGHTENED":
                if self.ghost.currentClydeMode != "EATEN":
                    return True
        return False

    def displayMap(self, pickups: Pickups) -> None:
        ghost = self.ghost
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                if self.player.currentX == x and self.player.currentY == y:
                    if pickups.pacgums[y][x] == 10:
                        self.specialData.score += 10
                        pickups.pacgums[y][x] = 0
                    elif pickups.pacgums[y][x] == 50:
                        self.specialData.score += 50
                        pickups.pacgums[y][x] = 0
                        ghost.setFrightenedMode()
                if self.map[y][x] == 1:
                    if ((str(y) + "y", str(x) + "x")) in self.wall42:
                        self.putImage(self.screen, x, y, "images/wall42.png")
                    else:
                        if (x > 0 and self.map[y][x - 1] == 1):
                            self.putImage(self.screen, x, y, "images/wall.png")
                        elif x < self.mapWidth - 1 and self.map[y][x + 1] == 1:
                            self.putImage(
                                self.screen,
                                x,
                                y,
                                "images/wall.png"
                            )
                        else:
                            self.putImage(self.screen, x, y, "images/wall.png")
                elif x == ghost.pinkyCurrentX and y == ghost.pinkyCurrentY:
                    if ghost.currentPinkyMode == "EATEN":
                        self.putImage(self.screen, x, y, "images/eaten.png")
                    elif ghost.currentPinkyMode == "FRIGHTENED":
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/Frightened.png"
                        )
                    else:
                        self.putImage(self.screen, x, y, "images/pinky.png")
                elif x == ghost.blinkyCurrentX and y == ghost.blinkyCurrentY:
                    if ghost.currentBlinkyMode == "EATEN":
                        self.putImage(self.screen, x, y, "images/eaten.png")
                    elif ghost.currentBlinkyMode == "FRIGHTENED":
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/Frightened.png"
                        )
                    else:
                        self.putImage(self.screen, x, y, "images/blinky.png")
                elif x == ghost.inkyCurrentX and y == ghost.inkyCurrentY:
                    if ghost.currentInkyMode == "EATEN":
                        self.putImage(self.screen, x, y, "images/eaten.png")
                    elif ghost.currentInkyMode == "FRIGHTENED":
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/Frightened.png"
                        )
                    else:
                        self.putImage(self.screen, x, y, "images/inky.png")
                elif x == ghost.clydeCurrentX and y == ghost.clydeCurrentY:
                    if ghost.currentClydeMode == "EATEN":
                        self.putImage(self.screen, x, y, "images/eaten.png")
                    elif ghost.currentClydeMode == "FRIGHTENED":
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/Frightened.png"
                        )
                    else:
                        self.putImage(self.screen, x, y, "images/clyde.png")
                elif self.player.currentX == x and self.player.currentY == y:
                    if self.player.nextDirection == "UP":
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/pacmantop.png"
                        )
                    elif self.player.nextDirection == "RIGHT":
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/pacmanright.png"
                        )
                    elif self.player.nextDirection == "LEFT":
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/pacmanleft.png"
                        )
                    else:
                        self.putImage(
                            self.screen,
                            x,
                            y,
                            "images/pacmanbottom.png"
                        )
                elif pickups.pacgums[y][x] == 10:
                    self.putImage(self.screen, x, y, "images/smallpickups.png")
                elif pickups.pacgums[y][x] == 50:
                    self.putImage(self.screen, x, y, "images/bigpickups.png")
        helperFloat = str(self.specialData.score)
        length = len(helperFloat) - 2
        if length < 0:
            length = 0
        specialFloat = 0.4 * length
        if specialFloat > 36:
            specialFloat = 0.5
        self.putString(
            self.screen,
            37 - specialFloat,
            0,
            f"                     score: {self.specialData.score}"
        )
        currentLevel = self.specialData.currentLevel + 1
        self.putString(
            self.screen,
            44.6,
            0,
            f" level: {currentLevel}/{self.specialData.allLevels}"
        )
        self.putString(
            self.screen,
            48.5,
            0,
            f" lives: {self.specialData.lives}"
        )
        if self.clock.pauseTimeCheateMode is False:
            if self.clock.pauseMenu is False:
                self.putString(
                    self.screen,
                    51.5,
                    0,
                    f" Time: {self.clock.getRemainingTime()}"
                )
