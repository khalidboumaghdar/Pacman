from typing import Any


class Game:
    def __init__(self, width: int, height: int, grid: list[list[int]], player: Any) -> None:
        self.width = width
        self.height = height
        self.grid = grid
        self.player = player
   
    def display_map(self) -> None:
        for y in range(self.height * 2 + 1):
            for x in range(self.width * 2 + 1):
                if self.grid[y][x] == 1:
                    print("*", end="")
                elif x == self.player.currentX and y == self.player.currentY:
                    print("P", end="")
                else:
                    print(" ", end="")
            print()
