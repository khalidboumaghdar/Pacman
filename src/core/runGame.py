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
from src.ui.menu import Resume_game, GameOver, VicotryWindow
from src.ui.renderer import Renderer
import json
from pathlib import Path


class RunGame:
    def __init__(self, renderer: Renderer):
        self.renderer: Renderer = renderer
        self.parser = Parser()
        self.config = self.parser.parse(sys.argv[1])
        self.levels = len(self.config["levels"])
        self.specialData = SpecialData(self.config["lives"])
        self.highscores: list = []
        self.vicotryWindow = None

    def runGameOverWindow(self) -> None:
        g = GameOver(self.renderer, self.specialData.score)
        name = g.show()
        # self.highscores["name"] = name
        # self.highscores["score"] = self.specialData.score
        # print(self.highscores)
        # with open(self.config["highscore_filename"], "a") as f:
        #     json.dump(self.highscores, f, indent=4)
        fl = Path(self.config["highscore_filename"])
        if fl.exists():
            with fl.open("r") as f:
                self.highscores = json.load(f)
        else:
            self.highscores = []

        self.highscores.append({
            "name": name,
            "score": self.specialData.score
        })
        with fl.open("w") as f:
            json.dump(self.highscores, f, indent=4)

    def runVicotryWindow(self) -> None:
        vicotryWindow = VicotryWindow(self.renderer, self.specialData.score)
        name = vicotryWindow.show()
        self.highscores.append({
            "name": name,
            "score": self.specialData.score
        })
        print(self.highscores)
        with open(self.config["highscore_filename"], "w") as f:
            json.dump(self.highscores, f, indent=4)
        print(name)

    def runGame(self) -> None:
        for i in range(self.levels):
            map_width = self.config["levels"][i]["width"]
            map_height = self.config["levels"][i]["height"]
            maze_adapter = MazeAdapter(
                size=(map_width, map_height),
                seed=self.config["seed"],
                level=i
            )
            map_width = (map_width * 2) + 1
            map_height = (map_height * 2) + 1
            ghost = Ghost(
                Entity(1, 1),
                Entity(map_width - 2, 1),
                Entity(1, map_height - 2),
                Entity(map_width - 2, map_height - 2)
            )
            player_entity = Entity(
                int((map_width - 1) / 2),
                int((map_height - 1) / 2)
            )
            player = Player(player_entity)
            clock = Clock(self.config["level_max_time"])
            game = Game(
                clock,
                map_width,
                map_height,
                player,
                ghost,
                self.specialData
            )
            game.buildGameMap(maze_adapter.get_maze())
            self.specialData.allLevels = self.levels
            pickups = Pickups(
                player,
                self.config["levels"][i].get("pacgum"),
                map_width,
                map_height,
                game.map,
                ghost
            )
            game.runGameWindow()
            p_menu = Resume_game(self.renderer)
            self.specialData.currentLevel = i
            while pickups.allPacgumsAreEaten() is False:
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
                    if game.isPaused is False:
                        if clock.pauseTimeCheateMode is False:
                            clock.oldTime += time.time() - clock.pauseTime
                            clock.pauseMenu = False
                    continue
                pygame.display.flip()
                player.previousDirection = player.nextDirection
                black = (0, 0, 0)
                game.screen.fill(black)
                if clock.getRemainingTime() <= 0:
                    if clock.pauseMenu is False \
                       and clock.pauseTimeCheateMode is False:
                        self.runGameOverWindow()
                        return
                if game.isRunning is False:
                    game.isRunning = True
                    self.specialData.lives -= 1
                    if self.specialData.lives <= 0:
                        time.sleep(0.4)
                        self.runGameOverWindow()
                        return
                    game.miniIntialize()
                game.detectKeyboardInput()
                game.movePacman()
                if game.checkIsPacmanEatedGhost() is True:
                    game.changeGhostModeToEaten()
                if game.checkIsAGhostEatedPacman() is True \
                   and game.c.check is False:
                    game.isRunning = False
                if clock.getRemainingTime() <= 0:
                    if clock.pauseMenu is False \
                       and clock.pauseTimeCheateMode is False:
                        self.runGameOverWindow()
                        return
                if game.isRunning is False:
                    try:
                        game.displayMap(pickups)
                    except Exception:
                        sys.exit()
                    pygame.display.flip()
                    black = (0, 0, 0)
                    game.screen.fill(black)
                    game.isRunning = True
                    self.specialData.lives -= 1
                    if self.specialData.lives <= 0:
                        time.sleep(0.4)
                        self.runGameOverWindow()
                        return
                    game.miniIntialize()
                ghost.prepareGhostsPossibleMoves(game.map)
                game.moveGhosts()
                try:
                    game.displayMap(pickups)
                except Exception:
                    sys.exit()
                if game.checkIsPacmanEatedGhost() is True:
                    game.changeGhostModeToEaten()
                if game.checkIsAGhostEatedPacman() is True \
                   and game.c.check is False:
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
        time.sleep(1)
        self.runVicotryWindow()
