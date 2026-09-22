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

    def displayMap(self, renderer: Any) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    self.pygamePygameStringPut(renderer.screen, x, y, "#")
                elif x == self.player.currentX and y == self.player.currentY:
                    self.pygamePygameStringPut(renderer.screen, x, y, "P")
                elif x == self.ghost.pinkyCurrentX and y == self.ghost.pinkyCurrentY:
                    self.pygamePygameStringPut(renderer.screen, x, y, "p")
                elif x == self.ghost.blinkyCurrentX and y == self.ghost.blinkyCurrentY:
                    self.pygamePygameStringPut(renderer.screen, x, y, "b")
                elif x == self.ghost.inkyCurrentX and y == self.ghost.inkyCurrentY:
                    self.pygamePygameStringPut(renderer.screen, x, y, "i")
                elif x == self.ghost.clydeCurrentX and y == self.ghost.clydeCurrentY:
                    self.pygamePygameStringPut(renderer.screen, x, y, "c")
                elif self.pickups.pacgums[y][x] == 10:
                    self.pygamePygameStringPut(renderer.screen, x, y, ".")
                elif self.pickups.pacgums[y][x] == 50:
                    self.pygamePygameStringPut(renderer.screen, x, y, "O")