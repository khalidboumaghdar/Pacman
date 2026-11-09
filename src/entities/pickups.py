import random
from src.entities.player import Player
from src.entities.ghost import Ghost


class Pickups:
    """the class that control the pacgums and super ones"""
    def __init__(
        self,
        player: Player,
        numberOfPacgum: int,
        width: int, height: int,
        map: list[list[int]],
        ghost: Ghost,
        points_per_pacgum: int,
        points_per_super_pacgum: int
    ) -> None:
        """ constructor method"""
        self.width = width
        self.height = height
        self.map = map
        self.ghost = ghost
        self.numberOfPacgum = numberOfPacgum
        self.player = player
        self.points_per_pacgum = points_per_pacgum
        self.points_per_super_pacgum = points_per_super_pacgum
        self.pacgums = self.build_pacgums()

    def build_pacgums(self) -> list[list[int]]:
        """build the pacgums"""
        mapsOpenCorridorsNumber = 0
        pacgums = [[0 for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if (
                    x == self.ghost.pinkyEntity.entityOriginalX
                    and y == self.ghost.pinkyEntity.entityOriginalY
                ):
                    pacgums[y][x] = self.points_per_super_pacgum
                elif (
                    x == self.ghost.blinkyEntity.entityOriginalX
                    and y == self.ghost.blinkyEntity.entityOriginalY
                ):
                    pacgums[y][x] = self.points_per_super_pacgum
                elif (
                    x == self.ghost.inkyEntity.entityOriginalX
                    and y == self.ghost.inkyEntity.entityOriginalY
                ):
                    pacgums[y][x] = self.points_per_super_pacgum
                elif (
                    x == self.ghost.clydeEntity.entityOriginalX
                    and y == self.ghost.clydeEntity.entityOriginalY
                ):
                    pacgums[y][x] = self.points_per_super_pacgum
                elif self.map[y][x] == 0:
                    if (
                        y == self.player.currentY and x == self.player.currentX
                    ):
                        pass
                    else:
                        mapsOpenCorridorsNumber += 1
        if self.numberOfPacgum > mapsOpenCorridorsNumber:
            for y in range(self.height):
                for x in range(self.width):
                    if (
                        x == self.ghost.pinkyEntity.entityOriginalX
                        and y == self.ghost.pinkyEntity.entityOriginalY
                    ):
                        continue
                    elif (
                        x == self.ghost.blinkyEntity.entityOriginalX
                        and y == self.ghost.blinkyEntity.entityOriginalY
                    ):
                        continue
                    elif (
                        x == self.ghost.inkyEntity.entityOriginalX
                        and y == self.ghost.inkyEntity.entityOriginalY
                    ):
                        continue
                    elif (
                        x == self.ghost.clydeEntity.entityOriginalX
                        and y == self.ghost.clydeEntity.entityOriginalY
                    ):
                        continue
                    elif self.map[y][x] == 0:
                        if (
                            y == self.player.currentY
                            and x == self.player.currentX
                        ):
                            continue
                        else:
                            pacgums[y][x] = self.points_per_pacgum
            return pacgums
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
                if (
                    pacgums[winner_row][winner_column] ==
                    self.points_per_super_pacgum
                ):
                    continue
                if (
                    pacgums[winner_row][winner_column] ==
                    self.points_per_pacgum
                ):
                    continue
                pacgums[winner_row][winner_column] = self.points_per_pacgum
                self.numberOfPacgum -= 1
        return pacgums

    def allPacgumsAreEaten(self) -> bool:
        """ check is all pacgums including supers ones, are
        removed all from current map"""
        for y in range(self.height):
            for x in range(self.width):
                if self.pacgums[y][x] != 0:
                    return False
        return True
