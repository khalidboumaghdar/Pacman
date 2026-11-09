from typing import Any
import pygame
import sys
from src.core.cheats import Cheat
import time
from src.core.clock import Clock
from src.entities.player import Player
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
from src.entities.specialData import SpecialData


class Game:
    """Game class that define behaviors
    and implement the whole game."""
    def __init__(
        self,
        clock: Clock,
        mapWidth: int,
        mapHeight: int,
        player: Player,
        ghost: Ghost,
        screen: Any,
        specialData: SpecialData,
        points_per_ghost: int,
        points_per_pacgum: int,
        points_per_super_pacgum: int
    ) -> None:
        """constructor method"""
        self.c = Cheat(False)
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.player = player
        self.ghost = ghost
        self.isRunning = True
        self.skyBlue = (175, 206, 235)
        self.screen = screen
        self.font = pygame.font.Font(None, 20)
        self.map: list
        self.clock = clock
        self.wall42: list = []
        self.specialData = specialData
        self.isPaused = False
        self.points_per_ghost = points_per_ghost
        self.points_per_pacgum = points_per_pacgum
        self.points_per_super_pacgum = points_per_super_pacgum

    def isThisA15CloseCell(
        self,
        generated_maze: list[list],
        column: int,
        row: int
    ) -> bool:
        if generated_maze[column][row]["N"] == 1:
            if generated_maze[column][row]["E"] == 1:
                if generated_maze[column][row]["S"] == 1:
                    if generated_maze[column][row]["W"] == 1:
                        return True
        return False

    def buildGameMap(self, generated_maze: list[list]) -> None:
        """build the game map """
        self.map = [
            [1 for x in range(self.mapWidth)] for y in range(self.mapHeight)
        ]
        for clums in range(len(generated_maze)):
            for rwo in range(len(generated_maze[0])):
                if generated_maze[clums][rwo]["N"] == 0:
                    self.map[(clums * 2 + 1) - 1][(rwo * 2 + 1)] = 0
                if generated_maze[clums][rwo]["E"] == 0:
                    self.map[(clums * 2 + 1)][(rwo * 2 + 1) + 1] = 0
                if generated_maze[clums][rwo]["S"] == 0:
                    self.map[(clums * 2 + 1) + 1][(rwo * 2 + 1)] = 0
                if generated_maze[clums][rwo]["W"] == 0:
                    self.map[(clums * 2 + 1)][(rwo * 2 + 1) - 1] = 0
                if (
                    self.isThisA15CloseCell(generated_maze, clums, rwo) == 1
                ):
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
                else:
                    self.map[(clums * 2 + 1)][(rwo * 2 + 1)] = 0
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
        """run the game window"""
        try:
            if self.screen is None:
                pygame.init()
                self.screen = pygame.display.set_mode(
                    (0, 0),
                    pygame.FULLSCREEN
                )
        except Exception as e:
            print(e)
            sys.exit()

    def detectKeyboardInput(self) -> None:
        """detect the keyboard input"""
        if self.countOpenDirections() > 2:
            time.sleep(0.03)
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

    def runAwayFromPacman(
            self,
            pickups: Pickups,
            ghost: str,
            goalX: int,
            goalY: int
    ) -> None:
        """run away from pacman"""
        GHOST = self.ghost
        if GHOST.frightenedCounter % 2 == 0:
            return
        if ghost == "pinky":
            pinkyNewPathCost = float("-inf")
            pinkyWinnerDirection = "None"
            for i in range(len(GHOST.pinkyPossibleMoves)):
                value = (GHOST.pinkyPossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.pinkyPossibleMoves[i][1] - goalY) ** 2
                if GHOST.previousPinkyX == GHOST.pinkyPossibleMoves[i][0]:
                    if GHOST.previousPinkyY == GHOST.pinkyPossibleMoves[i][1]:
                        if (value > 4):
                            continue
                if pinkyNewPathCost < value:
                    pinkyNewPathCost = value
                    pinkyWinnerDirection = GHOST.pinkyPossibleMoves[i][2]
            GHOST.previousPinkyX = GHOST.pinkyCurrentX
            GHOST.previousPinkyY = GHOST.pinkyCurrentY
            self.putImage(
                self.screen,
                GHOST.previousPinkyX,
                GHOST.previousPinkyY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousPinkyY]
                [GHOST.previousPinkyX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousPinkyX,
                    GHOST.previousPinkyY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousPinkyY]
                [GHOST.previousPinkyX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousPinkyX,
                    GHOST.previousPinkyY,
                    "images/bigpickups.png"
                )
            if pinkyWinnerDirection == "UP":
                GHOST.pinkyCurrentY -= 1
            elif pinkyWinnerDirection == "RIGHT":
                GHOST.pinkyCurrentX += 1
            elif pinkyWinnerDirection == "LEFT":
                GHOST.pinkyCurrentX -= 1
            elif pinkyWinnerDirection == "DOWN":
                GHOST.pinkyCurrentY += 1
        elif ghost == "blinky":
            blinkyNewPathCost = float("-inf")
            blinkyWinnerDirection = "None"
            for i in range(len(GHOST.blinkyPossibleMoves)):
                value = (GHOST.blinkyPossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.blinkyPossibleMoves[i][1] - goalY) ** 2
                if GHOST.previousBlinkyX == GHOST.blinkyPossibleMoves[i][0]:
                    if (
                        GHOST.previousBlinkyY
                        == GHOST.blinkyPossibleMoves[i][1]
                    ):
                        if (value > 4):
                            continue
                if blinkyNewPathCost < value:
                    blinkyNewPathCost = value
                    blinkyWinnerDirection = GHOST.blinkyPossibleMoves[i][2]
            GHOST.previousBlinkyX = GHOST.blinkyCurrentX
            GHOST.previousBlinkyY = GHOST.blinkyCurrentY
            self.putImage(
                self.screen,
                GHOST.previousBlinkyX,
                GHOST.previousBlinkyY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousBlinkyY]
                [GHOST.previousBlinkyX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousBlinkyX,
                    GHOST.previousBlinkyY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousBlinkyY]
                [GHOST.previousBlinkyX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousBlinkyX,
                    GHOST.previousBlinkyY,
                    "images/bigpickups.png"
                )
            if blinkyWinnerDirection == "UP":
                GHOST.blinkyCurrentY -= 1
            elif blinkyWinnerDirection == "RIGHT":
                GHOST.blinkyCurrentX += 1
            elif blinkyWinnerDirection == "LEFT":
                GHOST.blinkyCurrentX -= 1
            elif blinkyWinnerDirection == "DOWN":
                GHOST.blinkyCurrentY += 1
        elif ghost == "inky":
            inkyNewPathCost = float("-inf")
            inkyWinnerDirection = "None"
            for i in range(len(GHOST.inkyPossibleMoves)):
                value = (GHOST.inkyPossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.inkyPossibleMoves[i][1] - goalY) ** 2
                if GHOST.previousInkyX == GHOST.inkyPossibleMoves[i][0]:
                    if GHOST.previousInkyY == GHOST.inkyPossibleMoves[i][1]:
                        if (value > 4):
                            continue
                if inkyNewPathCost < value:
                    inkyNewPathCost = value
                    inkyWinnerDirection = GHOST.inkyPossibleMoves[i][2]
            GHOST.previousInkyX = GHOST.inkyCurrentX
            GHOST.previousInkyY = GHOST.inkyCurrentY
            self.putImage(
                self.screen,
                GHOST.previousInkyX,
                GHOST.previousInkyY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousInkyY]
                [GHOST.previousInkyX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousInkyX,
                    GHOST.previousInkyY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousInkyY]
                [GHOST.previousInkyX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousInkyX,
                    GHOST.previousInkyY,
                    "images/bigpickups.png"
                )
            if inkyWinnerDirection == "UP":
                GHOST.inkyCurrentY -= 1
            elif inkyWinnerDirection == "RIGHT":
                GHOST.inkyCurrentX += 1
            elif inkyWinnerDirection == "LEFT":
                GHOST.inkyCurrentX -= 1
            elif inkyWinnerDirection == "DOWN":
                GHOST.inkyCurrentY += 1
        elif ghost == "clyde":
            clydeNewPathCost = float("-inf")
            clydeWinnerDirection = "None"
            for i in range(len(GHOST.clydePossibleMoves)):
                value = (GHOST.clydePossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.clydePossibleMoves[i][1] - goalY) ** 2
                if GHOST.previousClydeX == GHOST.clydePossibleMoves[i][0]:
                    if GHOST.previousClydeY == GHOST.clydePossibleMoves[i][1]:
                        if (value > 4):
                            continue
                if clydeNewPathCost < value:
                    clydeNewPathCost = value
                    clydeWinnerDirection = GHOST.clydePossibleMoves[i][2]
            GHOST.previousClydeX = GHOST.clydeCurrentX
            GHOST.previousClydeY = GHOST.clydeCurrentY
            self.putImage(
                self.screen,
                GHOST.previousClydeX,
                GHOST.previousClydeY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousClydeY]
                [GHOST.previousClydeX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousClydeX,
                    GHOST.previousClydeY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousClydeY]
                [GHOST.previousClydeX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousClydeX,
                    GHOST.previousClydeY,
                    "images/bigpickups.png"
                )
            if clydeWinnerDirection == "UP":
                GHOST.clydeCurrentY -= 1
            elif clydeWinnerDirection == "RIGHT":
                GHOST.clydeCurrentX += 1
            elif clydeWinnerDirection == "LEFT":
                GHOST.clydeCurrentX -= 1
            elif clydeWinnerDirection == "DOWN":
                GHOST.clydeCurrentY += 1

    def changeGhostModeToEaten(self) -> None:
        """change ghost mode to eaten mode"""
        if self.player.currentX == self.ghost.pinkyCurrentX:
            if self.player.currentY == self.ghost.pinkyCurrentY:
                self.ghost.currentPinkyMode = "EATEN"
                self.ghost.pinkyCounter = 0
        if self.player.currentX == self.ghost.blinkyCurrentX:
            if self.player.currentY == self.ghost.blinkyCurrentY:
                self.ghost.currentBlinkyMode = "EATEN"
                self.ghost.blinkyCounter = 0
        if self.player.currentX == self.ghost.inkyCurrentX:
            if self.player.currentY == self.ghost.inkyCurrentY:
                self.ghost.currentInkyMode = "EATEN"
                self.ghost.inkyCounter = 0
        if self.player.currentX == self.ghost.clydeCurrentX:
            if self.player.currentY == self.ghost.clydeCurrentY:
                self.ghost.currentClydeMode = "EATEN"
                self.ghost.clydeCounter = 0

    def countOpenDirections(self) -> int:
        count = 0
        y = int(self.player.currentY - 1)
        x = int(self.player.currentX)
        if (self.map[y][x] == 0):
            count += 1
        y = int(self.player.currentY)
        x = int(self.player.currentX + 1)
        if (self.map[y][x] == 0):
            count += 1
        y = int(self.player.currentY + 1)
        x = int(self.player.currentX)
        if (self.map[y][x] == 0):
            count += 1
        y = int(self.player.currentY)
        x = int(self.player.currentX - 1)
        if (self.map[y][x] == 0):
            count += 1
        return count

    def isDirectionOpen(self, direction: str) -> bool:
        """is direction open or close"""
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

    def removeGhostsFromMap(self) -> None:
        """remove ghosts from map to reset the characters"""
        self.putImage(
            self.screen,
            self.ghost.pinkyCurrentX,
            self.ghost.pinkyCurrentY,
            "images/black.png"
        )
        self.putImage(
            self.screen,
            self.ghost.blinkyCurrentX,
            self.ghost.blinkyCurrentY,
            "images/black.png"
        )
        self.putImage(
            self.screen,
            self.ghost.inkyCurrentX,
            self.ghost.inkyCurrentY,
            "images/black.png"
        )
        self.putImage(
            self.screen,
            self.ghost.clydeCurrentX,
            self.ghost.clydeCurrentY,
            "images/black.png"
        )

    def miniIntialize(self) -> None:
        """reset and initialzie the characters"""
        time.sleep(0.7)
        self.removeGhostsFromMap()
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
        """move pacman in map"""
        if self.isDirectionOpen(self.player.ignoredDirection) is True:
            self.player.nextDirection = self.player.ignoredDirection
            self.player.ignoredDirection = "None"
        self.putImage(
            self.screen,
            self.player.currentX,
            self.player.currentY,
            "images/black.png"
        )
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
        """put the image in the map"""
        myImage = pygame.image.load(image)
        x = int((x + ((95 - self.mapWidth) / 2)) * 20)
        y = int((y + ((53 - self.mapHeight) / 2)) * 20)
        window.blit(myImage, (x, y))

    def checkIsPacmanEatedGhost(self) -> bool:
        """check is pacman eated ghost"""
        if self.player.currentX == self.ghost.pinkyCurrentX:
            if self.player.currentY == self.ghost.pinkyCurrentY:
                if self.ghost.currentPinkyMode == "FRIGHTENED":
                    self.specialData.score += self.points_per_ghost
                    return True
        if self.player.currentX == self.ghost.blinkyCurrentX:
            if self.player.currentY == self.ghost.blinkyCurrentY:
                if self.ghost.currentBlinkyMode == "FRIGHTENED":
                    self.specialData.score += self.points_per_ghost
                    return True
        if self.player.currentX == self.ghost.inkyCurrentX:
            if self.player.currentY == self.ghost.inkyCurrentY:
                if self.ghost.currentInkyMode == "FRIGHTENED":
                    self.specialData.score += self.points_per_ghost
                    return True
        if self.player.currentX == self.ghost.clydeCurrentX:
            if self.player.currentY == self.ghost.clydeCurrentY:
                if self.ghost.currentClydeMode == "FRIGHTENED":
                    self.specialData.score += self.points_per_ghost
                    return True
        return False

    def displayMapInfastructor(self, pickups: Pickups) -> None:
        """display map infastructor including the walls"""
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
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
                elif pickups.pacgums[y][x] == self.points_per_pacgum:
                    self.putImage(self.screen, x, y, "images/smallpickups.png")
                elif pickups.pacgums[y][x] == self.points_per_super_pacgum:
                    self.putImage(self.screen, x, y, "images/bigpickups.png")

    def putString(self, window: Any, x: float, y: float, string: str) -> None:
        """put the string in the game interface window"""
        text = self.font.render(string, True, self.skyBlue)
        window.blit(text, (x * 20, y * 20))

    def MoveGhostToTarget(
            self,
            pickups: Pickups,
            ghost: str,
            goalX: int,
            goalY: int
    ) -> None:
        """ move ghosts to the target"""
        GHOST = self.ghost
        if GHOST.chaseCounter % 3 == 0:
            return
        if ghost == "pinky":
            pinkyNewPathCost = float("inf")
            pinkyWinnerDirection = "None"
            for i in range(len(GHOST.pinkyPossibleMoves)):
                if GHOST.previousPinkyX == GHOST.pinkyPossibleMoves[i][0]:
                    if GHOST.previousPinkyY == GHOST.pinkyPossibleMoves[i][1]:
                        continue
                value = (GHOST.pinkyPossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.pinkyPossibleMoves[i][1] - goalY) ** 2
                if pinkyNewPathCost > value:
                    pinkyNewPathCost = value
                    pinkyWinnerDirection = GHOST.pinkyPossibleMoves[i][2]
            GHOST.previousPinkyX = GHOST.pinkyCurrentX
            GHOST.previousPinkyY = GHOST.pinkyCurrentY
            self.putImage(
                self.screen,
                GHOST.previousPinkyX,
                GHOST.previousPinkyY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousPinkyY]
                [GHOST.previousPinkyX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousPinkyX,
                    GHOST.previousPinkyY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousPinkyY]
                [GHOST.previousPinkyX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousPinkyX,
                    GHOST.previousPinkyY,
                    "images/bigpickups.png"
                )
            if pinkyWinnerDirection == "UP":
                GHOST.pinkyCurrentY -= 1
            elif pinkyWinnerDirection == "RIGHT":
                GHOST.pinkyCurrentX += 1
            elif pinkyWinnerDirection == "LEFT":
                GHOST.pinkyCurrentX -= 1
            elif pinkyWinnerDirection == "DOWN":
                GHOST.pinkyCurrentY += 1
        elif ghost == "blinky":
            blinkyNewPathCost = float("inf")
            blinkyWinnerDirection = "None"
            for i in range(len(GHOST.blinkyPossibleMoves)):
                if GHOST.previousBlinkyX == GHOST.blinkyPossibleMoves[i][0]:
                    if (
                        GHOST.previousBlinkyY
                        == GHOST.blinkyPossibleMoves[i][1]
                    ):
                        continue
                value = (GHOST.blinkyPossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.blinkyPossibleMoves[i][1] - goalY) ** 2
                if blinkyNewPathCost > value:
                    blinkyNewPathCost = value
                    blinkyWinnerDirection = GHOST.blinkyPossibleMoves[i][2]
            GHOST.previousBlinkyX = GHOST.blinkyCurrentX
            GHOST.previousBlinkyY = GHOST.blinkyCurrentY
            self.putImage(
                self.screen,
                GHOST.previousBlinkyX,
                GHOST.previousBlinkyY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousBlinkyY]
                [GHOST.previousBlinkyX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousBlinkyX,
                    GHOST.previousBlinkyY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousBlinkyY]
                [GHOST.previousBlinkyX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousBlinkyX,
                    GHOST.previousBlinkyY,
                    "images/bigpickups.png"
                )
            if blinkyWinnerDirection == "UP":
                GHOST.blinkyCurrentY -= 1
            elif blinkyWinnerDirection == "RIGHT":
                GHOST.blinkyCurrentX += 1
            elif blinkyWinnerDirection == "LEFT":
                GHOST.blinkyCurrentX -= 1
            elif blinkyWinnerDirection == "DOWN":
                GHOST.blinkyCurrentY += 1
        elif ghost == "inky":
            inkyNewPathCost = float("inf")
            inkyWinnerDirection = "None"
            for i in range(len(GHOST.inkyPossibleMoves)):
                if GHOST.previousInkyX == GHOST.inkyPossibleMoves[i][0]:
                    if GHOST.previousInkyY == GHOST.inkyPossibleMoves[i][1]:
                        continue
                value = (GHOST.inkyPossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.inkyPossibleMoves[i][1] - goalY) ** 2
                if inkyNewPathCost > value:
                    inkyNewPathCost = value
                    inkyWinnerDirection = GHOST.inkyPossibleMoves[i][2]
            GHOST.previousInkyX = GHOST.inkyCurrentX
            GHOST.previousInkyY = GHOST.inkyCurrentY
            self.putImage(
                self.screen,
                GHOST.previousInkyX,
                GHOST.previousInkyY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousInkyY]
                [GHOST.previousInkyX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousInkyX,
                    GHOST.previousInkyY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousInkyY]
                [GHOST.previousInkyX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousInkyX,
                    GHOST.previousInkyY,
                    "images/bigpickups.png"
                )
            if inkyWinnerDirection == "UP":
                GHOST.inkyCurrentY -= 1
            elif inkyWinnerDirection == "RIGHT":
                GHOST.inkyCurrentX += 1
            elif inkyWinnerDirection == "LEFT":
                GHOST.inkyCurrentX -= 1
            elif inkyWinnerDirection == "DOWN":
                GHOST.inkyCurrentY += 1
        elif ghost == "clyde":
            clydeNewPathCost = float("inf")
            clydeWinnerDirection = "None"
            for i in range(len(GHOST.clydePossibleMoves)):
                if GHOST.previousClydeX == GHOST.clydePossibleMoves[i][0]:
                    if GHOST.previousClydeY == GHOST.clydePossibleMoves[i][1]:
                        continue
                value = (GHOST.clydePossibleMoves[i][0] - goalX) ** 2
                value += (GHOST.clydePossibleMoves[i][1] - goalY) ** 2
                if clydeNewPathCost > value:
                    clydeNewPathCost = value
                    clydeWinnerDirection = GHOST.clydePossibleMoves[i][2]
            GHOST.previousClydeX = GHOST.clydeCurrentX
            GHOST.previousClydeY = GHOST.clydeCurrentY
            self.putImage(
                self.screen,
                GHOST.previousClydeX,
                GHOST.previousClydeY,
                "images/black.png"
            )
            if (
                pickups.pacgums[GHOST.previousClydeY]
                [GHOST.previousClydeX] == self.points_per_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousClydeX,
                    GHOST.previousClydeY,
                    "images/smallpickups.png"
                )
            elif (
                pickups.pacgums[GHOST.previousClydeY]
                [GHOST.previousClydeX] == self.points_per_super_pacgum
            ):
                self.putImage(
                    self.screen,
                    GHOST.previousClydeX,
                    GHOST.previousClydeY,
                    "images/bigpickups.png"
                )
            if clydeWinnerDirection == "UP":
                GHOST.clydeCurrentY -= 1
            elif clydeWinnerDirection == "RIGHT":
                GHOST.clydeCurrentX += 1
            elif clydeWinnerDirection == "LEFT":
                GHOST.clydeCurrentX -= 1
            elif clydeWinnerDirection == "DOWN":
                GHOST.clydeCurrentY += 1

    def moveGhosts(self, pickups: Pickups) -> None:
        """move ghosts depending on thier modes"""
        self.ghost.frightenedCounter += 1
        self.ghost.chaseCounter += 1
        if self.ghost.currentPinkyMode == "SCATTER":
            self.MoveGhostToTarget(pickups, "pinky", 0, 0)
        elif self.ghost.currentPinkyMode == "CHASE":
            self.MoveGhostToTarget(
                pickups,
                "pinky",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentPinkyMode == "FRIGHTENED":
            self.runAwayFromPacman(
                pickups,
                "pinky",
                self.player.currentX,
                self.player.currentY
            )
        if self.ghost.currentBlinkyMode == "SCATTER":
            self.MoveGhostToTarget(
                pickups,
                "blinky",
                self.mapWidth - 1,
                0
            )
        elif self.ghost.currentBlinkyMode == "CHASE":
            self.MoveGhostToTarget(
                pickups,
                "blinky",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentBlinkyMode == "FRIGHTENED":
            self.runAwayFromPacman(
                pickups,
                "blinky",
                self.player.currentX,
                self.player.currentY
            )
        if self.ghost.currentInkyMode == "SCATTER":
            self.MoveGhostToTarget(
                pickups,
                "inky",
                0,
                self.mapHeight - 1
            )
        elif self.ghost.currentInkyMode == "CHASE":
            self.MoveGhostToTarget(
                pickups,
                "inky",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentInkyMode == "FRIGHTENED":
            self.runAwayFromPacman(
                pickups,
                "inky",
                self.player.currentX,
                self.player.currentY
            )
        if self.ghost.currentClydeMode == "SCATTER":
            self.MoveGhostToTarget(
                pickups,
                "clyde",
                self.mapWidth - 1,
                self.mapHeight - 1
            )
        elif self.ghost.currentClydeMode == "CHASE":
            self.MoveGhostToTarget(
                pickups,
                "clyde",
                self.player.currentX,
                self.player.currentY
            )
        elif self.ghost.currentClydeMode == "FRIGHTENED":
            self.runAwayFromPacman(
                pickups,
                "clyde",
                self.player.currentX,
                self.player.currentY
            )

    def checkIsAGhostEatedPacman(self, pickups: Pickups) -> bool:
        """check is a ghost eated pacman"""
        player = self.player
        ghost = self.ghost
        if self.ghost.currentPinkyMode == "EATEN":
            if (
                ghost.pinkyEntity.entityOriginalX == player.currentX
                and
                ghost.pinkyEntity.entityOriginalY == player.currentY
            ):
                if ghost.pinkyCounter >= 76:
                    self.putImage(
                        self.screen,
                        player.currentX,
                        player.currentY,
                        "images/pinky.png"
                    )
                    return True
        if self.ghost.currentBlinkyMode == "EATEN":
            if (
                ghost.blinkyEntity.entityOriginalX == player.currentX
                and
                ghost.blinkyEntity.entityOriginalY == player.currentY
            ):
                if ghost.blinkyCounter >= 76:
                    self.putImage(
                        self.screen,
                        player.currentX,
                        player.currentY,
                        "images/blinky.png"
                    )
                    return True
        if self.ghost.currentInkyMode == "EATEN":
            if (
                ghost.inkyEntity.entityOriginalX == player.currentX
                and
                ghost.inkyEntity.entityOriginalY == player.currentY
            ):
                if ghost.inkyCounter >= 76:
                    self.putImage(
                        self.screen,
                        player.currentX,
                        player.currentY,
                        "images/inky.png"
                    )
                    return True
        if self.ghost.currentClydeMode == "EATEN":
            if (
                ghost.clydeEntity.entityOriginalX == player.currentX
                and
                ghost.clydeEntity.entityOriginalY == player.currentY
            ):
                if ghost.clydeCounter >= 76:
                    self.putImage(
                        self.screen,
                        player.currentX,
                        player.currentY,
                        "images/clyde.png"
                    )
                    return True
        if (
            pickups.pacgums[player.currentY]
            [player.currentX] == self.points_per_pacgum
        ):
            return False
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

    def clearSpecialData(self) -> None:
        """clear special data including available lives etc..."""
        self.screen.fill((0, 0, 0), ((0, 0), (2000, 12)))

    def displayMap(self, pickups: Pickups) -> None:
        """display the map in the game interface window"""
        ghost = self.ghost
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                if self.player.currentX == x and self.player.currentY == y:
                    if pickups.pacgums[y][x] == self.points_per_pacgum:
                        self.specialData.score += self.points_per_pacgum
                        pickups.pacgums[y][x] = 0
                    elif pickups.pacgums[y][x] == self.points_per_super_pacgum:
                        self.putImage(self.screen, x, y, "images/black.png")
                        self.specialData.score += self.points_per_super_pacgum
                        pickups.pacgums[y][x] = 0
                        ghost.setFrightenedMode()
                if x == ghost.pinkyCurrentX and y == ghost.pinkyCurrentY:
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
        self.clearSpecialData()
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
            f"                     Score: {self.specialData.score}"
        )
        currentLevel = self.specialData.currentLevel + 1
        self.putString(
            self.screen,
            44.6,
            0,
            f" Level: {currentLevel}/{self.specialData.allLevels}"
        )
        if self.c.check is False:
            self.putString(
                self.screen,
                48.5,
                0,
                f" Lives: {self.specialData.lives}"
            )
        if self.clock.pauseTimeCheateMode is False:
            if self.clock.pauseMenu is False:
                self.putString(
                    self.screen,
                    51.5,
                    0,
                    f" Time: {self.clock.getRemainingTime()}"
                )
        pygame.display.flip()

    def updateGhostModesIfNecessary(self) -> None:
        """update ghost modes if necessary etc..."""
        GHOST = self.ghost
        GHOST.pinkyCounter += 1
        if GHOST.pinkyCounter == 116 and GHOST.currentPinkyMode == "SCATTER":
            GHOST.pinkyCounter = 0
            GHOST.currentPinkyMode = "CHASE"
            GHOST.initialize_ghosts("pinky")
        elif GHOST.pinkyCounter == 333 and GHOST.currentPinkyMode == "CHASE":
            GHOST.pinkyCounter = 0
            GHOST.currentPinkyMode = "SCATTER"
            GHOST.initialize_ghosts("pinky")
        elif (
            GHOST.pinkyCounter == 149
            and GHOST.currentPinkyMode == "FRIGHTENED"
        ):
            GHOST.pinkyCounter = GHOST.previousPinkyCounterValue
            GHOST.currentPinkyMode = GHOST.previousPinkyMode
            GHOST.initialize_ghosts("pinky")
        elif GHOST.pinkyCounter == 83 and GHOST.currentPinkyMode == "EATEN":
            self.putImage(
                self.screen,
                GHOST.pinkyCurrentX,
                GHOST.pinkyCurrentY,
                "images/black.png"
            )
            original_x = GHOST.pinkyEntity.entityOriginalX
            GHOST.pinkyCurrentX = original_x
            original_y = GHOST.pinkyEntity.entityOriginalY
            GHOST.pinkyCurrentY = original_y
            GHOST.pinkyCounter = GHOST.previousPinkyCounterValue
            GHOST.currentPinkyMode = GHOST.previousPinkyMode
            GHOST.initialize_ghosts("pinky")
        elif (
            GHOST.pinkyCounter == 76
            and GHOST.currentPinkyMode == "EATEN"
        ):
            self.putImage(
                self.screen,
                GHOST.pinkyEntity.entityOriginalX,
                GHOST.pinkyEntity.entityOriginalY,
                "images/pinky.png"
            )
        GHOST.blinkyCounter += 1
        if GHOST.blinkyCounter == 116 and GHOST.currentBlinkyMode == "SCATTER":
            GHOST.blinkyCounter = 0
            GHOST.currentBlinkyMode = "CHASE"
            GHOST.initialize_ghosts("blinky")
        elif GHOST.blinkyCounter == 333 and GHOST.currentBlinkyMode == "CHASE":
            GHOST.blinkyCounter = 0
            GHOST.currentBlinkyMode = "SCATTER"
            GHOST.initialize_ghosts("blinky")
        elif (
            GHOST.blinkyCounter == 149
            and GHOST.currentBlinkyMode == "FRIGHTENED"
        ):
            GHOST.blinkyCounter = \
                GHOST.previousBlinkyCounterValue
            GHOST.currentBlinkyMode = GHOST.previousBlinkyMode
            GHOST.initialize_ghosts("blinky")
        elif GHOST.blinkyCounter == 83 and GHOST.currentBlinkyMode == "EATEN":
            self.putImage(
                self.screen,
                GHOST.blinkyCurrentX,
                GHOST.blinkyCurrentY,
                "images/black.png"
            )
            original_x = GHOST.blinkyEntity.entityOriginalX
            GHOST.blinkyCurrentX = original_x
            original_y = GHOST.blinkyEntity.entityOriginalY
            GHOST.blinkyCurrentY = original_y
            GHOST.blinkyCounter = GHOST.previousBlinkyCounterValue
            GHOST.currentBlinkyMode = GHOST.previousBlinkyMode
            GHOST.initialize_ghosts("blinky")
        elif (
            GHOST.blinkyCounter == 76
            and GHOST.currentBlinkyMode == "EATEN"
        ):
            self.putImage(
                self.screen,
                GHOST.blinkyEntity.entityOriginalX,
                GHOST.blinkyEntity.entityOriginalY,
                "images/blinky.png"
            )
        GHOST.inkyCounter += 1
        if GHOST.inkyCounter == 116 and GHOST.currentInkyMode == "SCATTER":
            GHOST.inkyCounter = 0
            GHOST.currentInkyMode = "CHASE"
            GHOST.initialize_ghosts("inky")
        elif GHOST.inkyCounter == 333 and GHOST.currentInkyMode == "CHASE":
            GHOST.inkyCounter = 0
            GHOST.currentInkyMode = "SCATTER"
            GHOST.initialize_ghosts("inky")
        elif (
            GHOST.inkyCounter == 149 and GHOST.currentInkyMode == "FRIGHTENED"
        ):
            GHOST.inkyCounter = GHOST.previousInkyCounterValue
            GHOST.currentInkyMode = GHOST.previousInkyMode
            GHOST.initialize_ghosts("inky")
        elif GHOST.inkyCounter == 83 and GHOST.currentInkyMode == "EATEN":
            self.putImage(
                self.screen,
                GHOST.inkyCurrentX,
                GHOST.inkyCurrentY,
                "images/black.png"
            )
            original_x = GHOST.inkyEntity.entityOriginalX
            GHOST.inkyCurrentX = original_x
            original_y = GHOST.inkyEntity.entityOriginalY
            GHOST.inkyCurrentY = original_y
            GHOST.inkyCounter = GHOST.previousInkyCounterValue
            GHOST.currentInkyMode = GHOST.previousInkyMode
            GHOST.initialize_ghosts("inky")
        elif (
            GHOST.inkyCounter == 76
            and GHOST.currentInkyMode == "EATEN"
        ):
            self.putImage(
                self.screen,
                GHOST.inkyEntity.entityOriginalX,
                GHOST.inkyEntity.entityOriginalY,
                "images/inky.png"
            )
        GHOST.clydeCounter += 1
        if GHOST.clydeCounter == 116 and GHOST.currentClydeMode == "SCATTER":
            GHOST.clydeCounter = 0
            GHOST.currentClydeMode = "CHASE"
            GHOST.initialize_ghosts("clyde")
        elif GHOST.clydeCounter == 333 and GHOST.currentClydeMode == "CHASE":
            GHOST.clydeCounter = 0
            GHOST.currentClydeMode = "SCATTER"
            GHOST.initialize_ghosts("clyde")
        elif (
            GHOST.clydeCounter == 149
            and GHOST.currentClydeMode == "FRIGHTENED"
        ):
            GHOST.clydeCounter = GHOST.previousClydeCounterValue
            GHOST.currentClydeMode = GHOST.previousClydeMode
            GHOST.initialize_ghosts("clyde")
        elif GHOST.clydeCounter == 83 and GHOST.currentClydeMode == "EATEN":
            self.putImage(
                self.screen,
                GHOST.clydeCurrentX,
                GHOST.clydeCurrentY,
                "images/black.png"
            )
            original_x = GHOST.clydeEntity.entityOriginalX
            GHOST.clydeCurrentX = original_x
            original_y = GHOST.clydeEntity.entityOriginalY
            GHOST.clydeCurrentY = original_y
            GHOST.clydeCounter = GHOST.previousClydeCounterValue
            GHOST.currentClydeMode = GHOST.previousClydeMode
            GHOST.initialize_ghosts("clyde")
        elif (
            GHOST.clydeCounter == 76
            and GHOST.currentClydeMode == "EATEN"
        ):
            self.putImage(
                self.screen,
                GHOST.clydeEntity.entityOriginalX,
                GHOST.clydeEntity.entityOriginalY,
                "images/clyde.png"
            )
