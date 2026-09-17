from src.core.game import Game
from src.config.loader import ConfigLoader
from src.maze.maze_model import MazeModel
import os

if __name__ == "__main__":
    configLoader = ConfigLoader("config.json")
    width = configLoader.config_data["levels"][0]["width"]
    height = configLoader.config_data["levels"][0]["height"]
    mazeModel = MazeModel(width, height, 50)
    grid = mazeModel.grid
    game = Game(width, height, grid)
    while 1:
        os.system("clear")
        game.display_map()