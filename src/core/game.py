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

    def movePacmanClearOldPosition(self, renderer: Any):
        if self.player.nextDirection == "UP":
            if (self.player.currentY - 1 == 0):
                return 
            self.player.currentY -= 1
        elif self.player.nextDirection == "RIGHT":
            if (self.player.currentX + 1 == self.width - 1):
                return
            self.player.currentX += 1
        elif self.player.nextDirection == "LEFT":
            if (self.player.currentX - 1 == 0):
                return
            self.player.currentX -= 1
        if self.player.nextDirection == "DOWN":
            if (self.player.currentY + 1 == self.height - 1):
                return
            self.player.currentY += 1

    def displayMap(self, renderer: Any) -> None:
        pygame.time.delay(100)
        font = pygame.font.Font('freesansbold.ttf', 20)
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    text = font.render("#", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)
                elif x == self.player.currentX and y == self.player.currentY:
                    text = font.render("P", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)
                elif x == self.ghost.pinkyCurrentX and y == self.ghost.pinkyCurrentY:
                    text = font.render("p", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)
                elif x == self.ghost.blinkyCurrentX and y == self.ghost.blinkyCurrentY:
                    text = font.render("b", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)
                elif x == self.ghost.inkyCurrentX and y == self.ghost.inkyCurrentY:
                    text = font.render("i", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)
                elif x == self.ghost.clydeCurrentX and y == self.ghost.clydeCurrentY:
                    text = font.render("c", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)
                elif self.pickups.pacgums[y][x] == 10:
                    text = font.render(".", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)
                elif self.pickups.pacgums[y][x] == 50:
                    text = font.render("O", True, self.white, self.black)
                    text_rect = text.get_rect()
                    text_rect.center = (x * 20, y * 20)
                    renderer.screen.blit(text, text_rect)