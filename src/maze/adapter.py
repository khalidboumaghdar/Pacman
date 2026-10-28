from typing import List
from mazegenerator import MazeGenerator


class MazeAdapter(MazeGenerator):
    """This class generates a maze using the mazegenerator package"""
    def __init__(
        self,
        size: tuple[int, int] = (15, 15),
        perfect: bool = False,
        seed: int = 0,
        level: int = 1
    ) -> None:
        if level != 1:
            seed = 0

        super().__init__(size=size, perfect=perfect, seed=seed)

    def get_maze(self) -> List[List[dict[str, int]]]:
        """This function retrieves the maze, determines directions,and checks
        whether a cell is a wall"""
        directions = {
            'N': 1,
            'E': 2,
            'S': 4,
            'W': 8
        }

        result: List[List[dict[str, int]]] = []
        for r in self.maze:
            new_row = []
            for c in r:
                new_cell = {}
                for key, v in directions.items():
                    if (c & v):
                        new_cell[key] = 1
                    else:
                        new_cell[key] = 0
                new_row.append(new_cell)
            result.append(new_row)

        return result
