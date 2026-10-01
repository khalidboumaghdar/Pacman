from typing import List
from mazegenerator import MazeGenerator


class MazeAdapter(MazeGenerator):
    def __init__(self, size: tuple[int, int] = (15, 15),
                 perfect: bool = False,
                 seed: int = 0,
                 level: int = 1
                 ) -> None:
        if level != 1:
            seed = 0
        super().__init__(size=size, perfect=perfect, seed=seed)

    def get_maze(self) -> List[List[int]]:
        directions = [1, 2, 4, 8]
        result: List[List[int]] = []
        
        height = len(self.maze)
        width = len(self.maze[0]) if height > 0 else 0
        for y, r in enumerate(self.maze):
            n_r: List[int] = []

            for x, cell in enumerate(r):
                
                if y == 0 or y == height - 1 or x == 0 or x == width - 1:
                    n_cell = 1
                    
                elif cell == 15:
                    n_cell = 4
            
                else:
                    for val in directions:
                        if (val & cell):
                            n_cell = 1
                        else:
                            n_cell = 0
                
                n_r.append(n_cell)
            result.append(n_r)

        return result


adapter1 = MazeAdapter(size=(25, 25), seed=55, level=1)
maze1 = adapter1.get_maze()

for m in maze1:
    print(m)