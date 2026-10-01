from src.core.game import Game
from src.config.loader import Loader
from src.entities.entity import Entity
from src.entities.player import Player
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
from src.maze.maze_model import MazeModel
import sys
import pygame


if __name__ == "__main__":
    loader = Loader("config.json")
    levels = len(loader.config_data["levels"])
    player = None
    for i in range(levels):
        width = loader.config_data["levels"][i]["width"]
        height = loader.config_data["levels"][i]["height"]
        mazeModel = MazeModel(width, height, 50)
        grid = mazeModel.grid
        width = (width * 2) + 1
        height = (height * 2) + 1
        player_entity = Entity((width - 1) / 2, (height - 1) / 2)
        if player == None:
            player = Player(player_entity)
        if player.lives == -1:
            player.lives = loader.config_data["lives"]
        player.allLevels = levels
        ghost = Ghost(
            Entity(1, 1), 
            Entity(width - 2, 1),
            Entity(1, height - 2),
            Entity(width - 2, height - 2)
        )
        pickups = Pickups(width, height, grid, ghost)
        game = Game(width, height, grid, player, ghost, pickups)
        game.runGameWindow()
        player.currentLevel = i
        while pickups.allPacgumsAreEaten() == False:
            pygame.display.update()
            player.previousDirection = player.nextDirection
            black = (0, 0, 0)
            game.screen.fill(black)
            if game.isRunning == False:
                pygame.time.delay(1000)
                game.isRunning = True
                player.lives -= 1
                if player.lives <= 0:
                    sys.exit()
                game.miniIntialize()
            game.detectKeyboardInput()
            game.movePacman()
            if game.checkIsPacmanEatedGhost() == True:
                game.changeGhostModeToEaten()
            if game.checkIsAGhostEatedPacman() == True:
                game.isRunning = False
            if game.isRunning == False:
                try:
                    game.displayMap()
                except Exception:
                    sys.exit()
                pygame.display.update()
                black = (0, 0, 0)
                game.screen.fill(black)
                pygame.time.delay(1000)
                game.isRunning = True
                player.lives -= 1
                if player.lives <= 0:
                    sys.exit()
                game.miniIntialize()
            ghost.prepareGhostsPossibleMoves(grid)
            game.moveGhosts()
            try:
                game.displayMap()
            except Exception:
                sys.exit()
            if game.checkIsPacmanEatedGhost() == True:
                game.changeGhostModeToEaten()
            if game.checkIsAGhostEatedPacman() == True:
                game.isRunning = False
            pygame.time.delay(60)
            print("\nPINKY current mode: ", ghost.currentPinkyMode, "\nBLINKY current mode: ", ghost.currentBlinkyMode, "\nINKY current mode: ", ghost.currentInkyMode, "\nCLYDE current mode: ", ghost.currentClydeMode)
            ghost.updateGhostModesIfNecessary()
        pygame.display.update()
        player.previousDirection = player.nextDirection
        black = (0, 0, 0)
        game.screen.fill(black)
        try:
            game.displayMap()
        except Exception:
            sys.exit()
        pygame.time.delay(2000)
