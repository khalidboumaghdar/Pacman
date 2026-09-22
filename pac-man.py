from src.core.game import Game
from src.config.loader import Loader
from src.entities.entity import Entity
from src.entities.player import Player
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
from src.maze.maze_model import MazeModel
from src.ui.renderer import Renderer
import pygame

if __name__ == "__main__":
    loader = Loader("config.json")
    width = loader.config_data["levels"][0]["width"]
    height = loader.config_data["levels"][0]["height"]
    mazeModel = MazeModel(width, height, 50)
    grid = mazeModel.grid
    width = (width * 2) + 1
    height = (height * 2) + 1
    player_entity = Entity((width - 1) / 2, (height - 1) / 2)
    player = Player(player_entity)
    ghost = Ghost(
        Entity(1, 1), 
        Entity(width - 2, 1),
        Entity(1, height - 2),
        Entity(width - 2, height - 2)
    )
    pickups = Pickups(width, height, grid, ghost)
    game = Game(width, height, grid, player, ghost, pickups)
    renderer = Renderer(player, game);
    while game.isRunning == True:
        pygame.display.update()
        pygame.time.delay(60)
        player.previousDirection = player.nextDirection
        black = (0, 0, 0)
        renderer.screen.fill(black)
        renderer.handleEvents()
        game.movePacman()
        if game.isRunning == True:
            game.displayMap(renderer)
