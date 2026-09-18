from typing import Any


class Game:
    def __init__(self, width: int, height: int, grid: list[list[int]], player: Any, ghost: Any) -> None:
        self.width = width
        self.height = height
        self.grid = grid
        self.player = player
        self.ghost = ghost
   
    def display_map(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    print("*", end="")
                elif x == self.player.currentX and y == self.player.currentY:
                    print("P", end="")
                elif x == self.ghost.pinkyCurrentX and y == self.ghost.pinkyCurrentY:
                    print("p", end="")
                elif x == self.ghost.blinkyCurrentX and y == self.ghost.blinkyCurrentY:
                    print("b", end="")
                elif x == self.ghost.inkyCurrentX and y == self.ghost.inkyCurrentY:
                    print("i", end="")
                elif x == self.ghost.clydeCurrentX and y == self.ghost.clydeCurrentY:
                    print("c", end="")
                else:
                    print(" ", end="")
            print()
