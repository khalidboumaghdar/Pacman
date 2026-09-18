from src.core.game import Game
from src.config.loader import Loader
from src.maze.maze_model import MazeModel
import os

if __name__ == "__main__":
    loader = Loader("config.json")
    width = loader.config_data["levels"][0]["width"]
    height = loader.config_data["levels"][0]["height"]
    mazeModel = MazeModel(width, height, 50)
    grid = mazeModel.grid
    game = Game(width, height, grid)
    while 1:
        os.system("clear")
        game.display_map()
