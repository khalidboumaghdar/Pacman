from src.core.game import Game
from src.config.loader import Loader
from src.entities.entity import Entity
from src.entities.player import Player
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
from src.maze.maze_model import MazeModel
from src.ui.renderer import Renderer
import sys
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
    while 1:
        pygame.display.update()
        player.previousDirection = player.nextDirection
        black = (0, 0, 0)
        renderer.screen.fill(black)
        if game.isRunning == False:
            break
        renderer.handleEvents()
        game.movePacman()
        if game.checkIsPacmanEatedGhost() == True:
            game.changeGhostModeToEaten()
        if game.checkIsAGhostEatedPacman() == True:
            game.isRunning = False
        if game.isRunning == False:
            try:
                game.displayMap(renderer)
            except Exception:
                sys.exit()
            pygame.display.update()
            black = (0, 0, 0)
            renderer.screen.fill(black)
            break
        ghost.prepareGhostsPossibleMoves(grid)
        game.moveGhosts()
        try:
            game.displayMap(renderer)
        except Exception:
            sys.exit()
        if game.checkIsPacmanEatedGhost() == True:
            game.changeGhostModeToEaten()
        if game.checkIsAGhostEatedPacman() == True:
            game.isRunning = False
        pygame.time.delay(60)
        print("\nPINKY: ", ghost.currentPinkyMode, "\nblinky: ", ghost.currentBlinkyMode, "\nINKY: ", ghost.currentInkyMode, "\nCLYDE: ", ghost.currentClydeMode)
        game.updateGhostModesIfNecessary()
    pygame.time.delay(2000)