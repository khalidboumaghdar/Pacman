from src.core.game import Game
from src.config.loader import Loader
from src.entities.entity import Entity
from src.entities.player import Player
from src.entities.ghost import Ghost
from src.maze.maze_model import MazeModel
import os


if __name__ == "__main__":
    loader = Loader("config.json")
    width = loader.config_data["levels"][0]["width"]
    height = loader.config_data["levels"][0]["height"]
    mazeModel = MazeModel(width, height, 50)
    width = (width * 2) + 1
    height = (height * 2) + 1
    player_entity = Entity((width - 1) / 2, (height - 1) / 2)
    player = Player(player_entity)
    grid = mazeModel.grid
    ghost = Ghost(
        Entity(1, 1), 
        Entity(width - 2, 1),
        Entity(1, height - 2),
        Entity(width - 2, height - 2)
    )
    game = Game(width, height, grid, player, ghost)
    while 1:
        os.system("clear")
        game.display_map()
