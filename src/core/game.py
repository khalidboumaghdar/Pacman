class Game:
    def __init__(self, width, height, grid) -> None:
        self.width = width
        self.height = height
        self.grid = grid
   
    def display_map(self) -> None:
        for y in range(self.height * 2 + 1):
            for x in range(self.width * 2 + 1):
                if self.grid[y][x] == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()