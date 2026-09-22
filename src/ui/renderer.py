import pygame
from typing import Any


class Renderer:
    def __init__(self, player: Any, game: Any):
        pygame.init()
        self.width = 1400
        self.height = 1200
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pac-man")
        
        # Clock for controlling FPS (e.g. 60 FPS)
        self.clock = pygame.time.Clock()
        self.player = player
        self.game = game

    def handleEvents(self) -> None:
        """Polls Pygame event queue every frame (replaces MLX setup_hooks)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeGame()
            elif event.type == pygame.KEYDOWN:
                self.handleKeyPress(event.key)

    def handleKeyPress(self, key: int) -> None:
        """Processes keyboard input."""
        if key in (pygame.K_w, pygame.K_UP):
            self.player.nextDirection = "UP"
        elif key in (pygame.K_s, pygame.K_DOWN):
            self.player.nextDirection = "DOWN"
        elif key in (pygame.K_a, pygame.K_LEFT):
            self.player.nextDirection = "LEFT"
        elif key in (pygame.K_d, pygame.K_RIGHT):
            self.player.nextDirection = "RIGHT"
        elif key == pygame.K_ESCAPE:
            self.closeGame()

    def closeGame(self) -> None:
        """Safely terminates Pygame and stops the game loop."""
        self.game.isRunning = False
        pygame.quit()
