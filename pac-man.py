from src.core.game import Game
from src.config.loader import Loader
from src.entities.entity import Entity
from src.entities.player import Player
from src.maze.maze_model import MazeModel
import os


if __name__ == "__main__":
    loader = Loader("config.json")
    width = loader.config_data["levels"][0]["width"]
    height = loader.config_data["levels"][0]["height"]
    mazeModel = MazeModel(width, height, 50)
    player_entity = Entity((width - 1) / 2, (height - 1) / 2)
    player = Player(player_entity)
    grid = mazeModel.grid
    game = Game(width, height, grid, player)
    while 1:
        os.system("clear")
        game.display_map()
