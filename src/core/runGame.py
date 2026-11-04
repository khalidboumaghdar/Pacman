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
    """RanGame class that implement
    game whole cycle"""
    def __init__(self, renderer: Renderer):
        """constructor method"""
        self.renderer: Renderer = renderer
        self.parser = Parser()
        if len(sys.argv) >= 2:
            self.config = self.parser.parse(sys.argv[1])
            if self.config:
                self.levels = len(self.config["levels"])
                self.specialData = SpecialData(self.config["lives"])
        else:
            self.config = self.parser.parse("")
            if self.config:
                self.levels = len(self.config["levels"])
                self.specialData = SpecialData(self.config["lives"])
        self.highscores: list = []
        self.vicotryWindow = None

    def runGameOverWindow(self) -> None:
        """run GameOver window"""
        g = GameOver(self.renderer, self.specialData.score)
        name = g.show()
        # self.highscores["name"] = name
        # self.highscores["score"] = self.specialData.score
        # print(self.highscores)
        # with open(self.config["highscore_filename"], "a") as f:
        #     json.dump(self.highscores, f, indent=4)
        if self.config:
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
        """run GameVicotry window"""
        vicotryWindow = VicotryWindow(self.renderer, self.specialData.score)
        name = vicotryWindow.show()
        self.highscores.append({
            "name": name,
            "score": self.specialData.score
        })
        if self.config:
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

    def runGame(self) -> None:
        """the most important method in the project,
        it run and start the game"""
        screen = None
        for i in range(self.levels):
            if self.config:
                map_width = self.config["levels"][i]["width"]
                map_height = self.config["levels"][i]["height"]
                maze_adapter = MazeAdapter(
                    size=(map_width, map_height),
                    seed=self.config["seed"],
                    level=i
                )
                # print(c)
                # print(maze_adapter._seed)
                # exit(0)
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
            if self.config:
                clock = Clock(self.config["level_max_time"])
            game = Game(
                clock,
                map_width,
                map_height,
                player,
                ghost,
                screen,
                self.specialData
            )
            game.buildGameMap(maze_adapter.get_maze())
            self.specialData.allLevels = self.levels
            if self.config:
                pickups = Pickups(
                    player,
                    self.config["levels"][i].get("pacgum"),
                    map_width,
                    map_height,
                    game.map,
                    ghost
                )
            game.runGameWindow()
            game.displayMapInfastructor(pickups)
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
                        game.screen.fill((0, 0, 0))
                        game.displayMapInfastructor(pickups)
                        if clock.pauseTimeCheateMode is False:
                            clock.oldTime += time.time() - clock.pauseTime
                            clock.pauseMenu = False
                    continue
                time.sleep(0.06)
                player.previousDirection = player.nextDirection
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
                if game.checkIsAGhostEatedPacman(pickups) is True \
                   and game.c.check is False:
                    game.isRunning = False
                game.displayMap(pickups)
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
                ghost.prepareGhostsPossibleMoves(game.map)
                game.moveGhosts(pickups)
                if game.checkIsPacmanEatedGhost() is True:
                    game.changeGhostModeToEaten()
                if game.checkIsAGhostEatedPacman(pickups) is True \
                   and game.c.check is False:
                    game.isRunning = False
                game.updateGhostModesIfNecessary()
                game.displayMap(pickups)
            screen = game.screen
            screen.fill((0, 0, 0))
            time.sleep(0.4)
        self.runVicotryWindow()
