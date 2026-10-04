from src.core.game import Game
from src.config.loader import Parser
from src.entities.entity import Entity
from src.entities.player import Player
from src.maze.adapter import MazeAdapter
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
import sys
import pygame


if __name__ == "__main__":
    parser = Parser()
    config = parser.parse(sys.argv[1])
    levels = len(config["levels"])
    player = None
    for i in range(levels):
        map_width = config["levels"][i]["width"]
        map_height = config["levels"][i]["height"]
        maze_adapter = MazeAdapter(size=(map_width, map_height), seed=55, level=i)
        map_width = (map_width * 2) + 1
        map_height = (map_height * 2) + 1
        ghost = Ghost(
            Entity(1, 1), 
            Entity(map_width - 2, 1),
            Entity(1, map_height - 2),
            Entity(map_width - 2, map_height - 2)
        )
        player_entity = Entity((map_width - 1) / 2, (map_height - 1) / 2)
        if player == None:
            player = Player(player_entity)
        if player.lives == -1:
            player.lives = config["lives"]
        game = Game(map_width, map_height, player, ghost)
        game.buildGameMap(maze_adapter.get_maze())
        player.allLevels = levels
        pickups = Pickups(map_width, map_height, game.map, ghost)
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
                    game.displayMap(pickups)
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
            ghost.prepareGhostsPossibleMoves(game.map)
            game.moveGhosts()
            try:
                game.displayMap(pickups)
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
            game.displayMap(pickups)
        except Exception:
            sys.exit()
        pygame.time.delay(2000)
