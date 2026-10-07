from typing import Any


class Pickups:
    def __init__(self, width: int, height: int, map: list[list[int]], ghost: Any) -> None:
        self.width = width
        self.height = height
        self.map = map
        self.ghost = ghost
        self.pacgums = self.build_pacgums()

    def build_pacgums(self) -> list[list[int]]:
        pacgums = [[0 for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if x == self.ghost.pinkyEntity.entityOriginalX and y == self.ghost.pinkyEntity.entityOriginalY:
                    pacgums[y][x] = 50
                elif x == self.ghost.blinkyEntity.entityOriginalX and y == self.ghost.blinkyEntity.entityOriginalY:
                    pacgums[y][x] = 50
                elif x == self.ghost.inkyEntity.entityOriginalX and y == self.ghost.inkyEntity.entityOriginalY:
                    pacgums[y][x] = 50
                elif x == self.ghost.clydeEntity.entityOriginalX and y == self.ghost.clydeEntity.entityOriginalY:
                    pacgums[y][x] = 50
                elif self.map[y][x] == 0:
                    pacgums[y][x] = 10
        return pacgums

    def allPacgumsAreEaten(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.pacgums[y][x] != 0:
                    return False
        return True