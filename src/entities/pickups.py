import random
from src.entities.player import Player
from src.entities.ghost import Ghost


class Pickups:
    def __init__(
        self,
        player: Player,
        numberOfPacgum: int,
        width: int, height: int,
        map: list[list[int]],
        ghost: Ghost
    ) -> None:
        self.width = width
        self.height = height
        self.map = map
        self.ghost = ghost
        self.numberOfPacgum = numberOfPacgum
        self.player = player
        self.pacgums = self.build_pacgums()

    def build_pacgums(self) -> list[list[int]]:
        pacgums = [[0 for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if (
                    x == self.ghost.pinkyEntity.entityOriginalX
                    and y == self.ghost.pinkyEntity.entityOriginalY
                ):
                    pacgums[y][x] = 50
                elif (
                    x == self.ghost.blinkyEntity.entityOriginalX
                    and y == self.ghost.blinkyEntity.entityOriginalY
                ):
                    pacgums[y][x] = 50
                elif (
                    x == self.ghost.inkyEntity.entityOriginalX
                    and y == self.ghost.inkyEntity.entityOriginalY
                ):
                    pacgums[y][x] = 50
                elif (
                    x == self.ghost.clydeEntity.entityOriginalX
                    and y == self.ghost.clydeEntity.entityOriginalY
                ):
                    pacgums[y][x] = 50
                elif self.map[y][x] == 0:
                    if self.numberOfPacgum is None:
                        pacgums[y][x] = 10
        if self.numberOfPacgum is not None:
            while self.numberOfPacgum > 0:
                y = 0
                random_rows = []
                while y < self.height:
                    random_rows.append(y)
                    y += 1
                winner_row = random.choice(random_rows)
                x = 0
                random_columns = []
                while x < self.width:
                    random_columns.append(x)
                    x += 1
                winner_column = random.choice(random_columns)
                if winner_row == self.player.entity.entityOriginalY:
                    if winner_column == self.player.entity.entityOriginalX:
                        continue
                if self.map[winner_row][winner_column] == 1:
                    continue
                if pacgums[winner_row][winner_column] == 50:
                    continue
                if pacgums[winner_row][winner_column] == 10:
                    continue
                pacgums[winner_row][winner_column] = 10
                self.numberOfPacgum -= 1
        return pacgums

    def allPacgumsAreEaten(self) -> bool:
        for y in range(self.height):
            for x in range(self.width):
                if self.pacgums[y][x] != 0:
                    return False
        return True
