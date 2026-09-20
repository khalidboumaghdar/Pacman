from typing import Any
from mlx import Mlx

class Game:
    def __init__(self, width: int, height: int, grid: list[list[int]], player: Any, ghost: Any, pickups: Any) -> None:
        self.width = width
        self.height = height
        self.grid = grid
        self.player = player
        self.ghost = ghost
        self.pickups = pickups
        self.isRunning = True

    def moveThePacman(self):
        if self.player.nextDirection == "UP":
            if (self.player.currentY - 1 == 0):
                return 
            self.player.currentY -= 1
        elif self.player.nextDirection == "RIGHT":
            if (self.player.currentX + 1 == self.width - 1):
                return
            self.player.currentX += 1
        if self.player.nextDirection == "LEFT":
            if (self.player.currentX - 1 == 0):
                return
            self.player.currentX -= 1
        if self.player.nextDirection == "DOWN":
            if (self.player.currentY + 1 == self.height - 1):
                return
            self.player.currentY += 1

   
    def displayMap(self, renderer: Any) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFF0000, "|")
                elif x == self.player.currentX and y == self.player.currentY:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFFFFFFFF, "P")
                elif x == self.ghost.pinkyCurrentX and y == self.ghost.pinkyCurrentY:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFFFFFFFF, "p")
                elif x == self.ghost.blinkyCurrentX and y == self.ghost.blinkyCurrentY:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFFFFFFFF, "b")
                elif x == self.ghost.inkyCurrentX and y == self.ghost.inkyCurrentY:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFFFFFFFF, "i")
                elif x == self.ghost.clydeCurrentX and y == self.ghost.clydeCurrentY:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFFFFFFFF, "c")
                elif self.pickups.pacgums[y][x] == 10:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFFFFFFFF, ".")
                elif self.pickups.pacgums[y][x] == 50:
                    renderer.mlx.mlx_string_put(renderer.mlx_ptr, renderer.win, x * 20, y * 20, 0xFFFFFFFF, "O")

    def gameLoop(self, renderer: Any):
        self.displayMap(renderer)
        renderer.mlx.mlx_clear_window(renderer.mlx_ptr, renderer.win)
        self.moveThePacman()

