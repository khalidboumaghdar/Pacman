from src.core.game import Game
from src.core.clock import Clock
from src.config.loader import Parser
from src.entities.entity import Entity
from src.entities.player import Player
from src.maze.adapter import MazeAdapter
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
from src.entities.specialData import SpecialData
import sys
import pygame
import time
from src.ui.menu import Resume_game, GameOver
from src.ui.renderer import Renderer


class RunGame:
    def __init__(self, renderer: Renderer):
        self.renderer: Renderer = renderer
        self.parser = Parser()
        self.config = self.parser.parse(sys.argv[1])
        self.levels = len(self.config["levels"])
        self.specialData = SpecialData(self.config["lives"])

    def runGame(self):
        for i in range(self.levels):
            map_width = self.config["levels"][i]["width"]
            map_height = self.config["levels"][i]["height"]
            maze_adapter = MazeAdapter(size=(map_width, map_height), seed=self.config["seed"], level=i)
            map_width = (map_width * 2) + 1
            map_height = (map_height * 2) + 1
            ghost = Ghost(
                Entity(1, 1), 
                Entity(map_width - 2, 1),
                Entity(1, map_height - 2),
                Entity(map_width - 2, map_height - 2)
            )
            player_entity = Entity(int((map_width - 1) / 2), int((map_height - 1) / 2))
            player = Player(player_entity)
            clock = Clock(self.config["level_max_time"])
            game = Game(clock, map_width, map_height, player, ghost, self.specialData)
            game.buildGameMap(maze_adapter.get_maze())
            self.specialData.allLevels = self.levels
            print(self.config["levels"][i]["pacgum"])
            pickups = Pickups(
                player, self.config["levels"][i].get("pacgum"), map_width, map_height, game.map, ghost
            )
            game.runGameWindow()
            p_menu = Resume_game(self.renderer)
            self.specialData.currentLevel = i
            while pickups.allPacgumsAreEaten() == False:
                if game.isPaused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_p:
                                game.isPaused = False
                            elif ev.key == pygame.K_UP:
                                p_menu.check_event("UP")
                            elif ev.key == pygame.K_DOWN:
                                p_menu.check_event("DOWN")
                            elif ev.key == pygame.K_RETURN:
                                result = p_menu.check_event("ENTER")
                                if result == "Resume the game":
                                    game.isPaused = False
                                elif result == "Return to the main menu":
                                    return

                    p_menu.draw()
                    time.sleep(0.05)
                    if game.isPaused == False:
                        clock.oldTime = clock.oldTime + (time.time() - clock.pauseTime)
                    continue
                pygame.display.flip()
                player.previousDirection = player.nextDirection
                black = (0, 0, 0)
                game.screen.fill(black)
                if clock.getRemainingTime() <= 0:
                    return
                if game.isRunning == False:
                    time.sleep(0.2)
                    game.isRunning = True
                    self.specialData.lives -= 1
                    if self.specialData.lives <= 0:
                        g = GameOver(self.renderer)
                        name = g.show()
                        print(name)
                        return
                    game.miniIntialize()
                game.detectKeyboardInput()
                game.movePacman()
                if game.checkIsPacmanEatedGhost() == True:
                    game.changeGhostModeToEaten()
                if game.checkIsAGhostEatedPacman() == True and game.c.check == False:
                    game.isRunning = False
                if clock.getRemainingTime() <= 0:
                    return
                if game.isRunning == False:
                    try:
                        game.displayMap(pickups)
                        p_menu.draw()
                    except Exception:
                        sys.exit()
                    pygame.display.flip()
                    black = (0, 0, 0)
                    game.screen.fill(black)
                    time.sleep(0.2)
                    game.isRunning = True
                    self.specialData.lives -= 1
                    if self.specialData.lives <= 0:
                        return
                    game.miniIntialize()
                ghost.prepareGhostsPossibleMoves(game.map)
                game.moveGhosts()
                try:
                    game.displayMap(pickups)
                except Exception:
                    sys.exit()
                if game.checkIsPacmanEatedGhost() == True:
                    game.changeGhostModeToEaten()
                if game.checkIsAGhostEatedPacman() == True and game.c.check == False:
                    game.isRunning = False
                time.sleep(0.06)
                ghost.updateGhostModesIfNecessary()
            pygame.display.flip()
            player.previousDirection = player.nextDirection
            black = (0, 0, 0)
            game.screen.fill(black)
            try:
                game.displayMap(pickups)
            except Exception:
                sys.exit()
            time.sleep(0.2)
