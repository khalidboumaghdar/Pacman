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
    counter = 0
    while game.isRunning == True:
        pygame.display.update()
        player.previousDirection = player.nextDirection
        black = (0, 0, 0)
        renderer.screen.fill(black)
        renderer.handleEvents()
        game.movePacman()
        ghost.prepareGhostsPossibleMoves(grid)
        if ghost.currentMode == "SCATTER":
            ghost.MoveGhostToTarget("pinky", 0, 0)
            ghost.MoveGhostToTarget("blinky", width - 1, 0)
            ghost.MoveGhostToTarget("inky", 0, height - 1)
            ghost.MoveGhostToTarget("clyde", width - 1, height - 1)
        elif ghost.currentMode == "CHASE":
            ghost.MoveGhostToTarget("pinky", player.currentX, player.currentY)
            ghost.MoveGhostToTarget("blinky", player.currentX, player.currentY)
            ghost.MoveGhostToTarget("inky", player.currentX, player.currentY)
            ghost.MoveGhostToTarget("clyde", player.currentX, player.currentY)
        if game.isRunning == True:
            game.displayMap(renderer)
        pygame.time.delay(60)
        counter += 1
        if counter == 116 and ghost.currentMode == "SCATTER":
            counter = 0
            ghost.currentMode = "CHASE"
        elif counter == 333 and ghost.currentMode == "CHASE":
            counter = 0
            ghost.currentMode = "SCATTER"