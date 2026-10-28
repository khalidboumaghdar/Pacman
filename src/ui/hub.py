from src.ui.renderer import Renderer
from src.ui.menu import Menu
from src.ui.screens import Score, Insruction
from src.core.runGame import RunGame
from typing import Optional, Any
from src.config.loader import Parser
import sys


class Hub:
    def __init__(self) -> None:
        self.renderer = Renderer(2000, 1500, "Pac-Man")
        self.menu = Menu(self.renderer)
        self.parser = Parser()
        if len(sys.argv[1]):
            self.config = self.parser.parse(sys.argv[1])
            if self.config:
                self.heghscore = self.config["highscore_filename"]
                self.score = Score(self.renderer,
                                   self.config["highscore_filename"])
        else:
            self.config = self.parser.parse("")
            if self.config:
                self.heghscore = self.config["highscore_filename"]
                self.score = Score(self.renderer,
                                   self.config["highscore_filename"])
        self.instruction = Insruction(self.renderer)
        self.screen = "MENU"
        self.run = True
        self.runGame: Optional[Any] = None

    def runMenu(self) -> None:
        while self.run:
            events = self.renderer.event()
            for event in events:
                if self.screen == "MENU":
                    result = self.menu.check_event(event)
                    if result == "START":
                        print("start game...")
                        try:
                            self.runGame = RunGame(self.renderer)
                            self.runGame.runGame()
                            self.renderer = Renderer(2000, 1500, "Pac-Man")
                        except Exception as e:
                            print(e)
                    elif result == "SCORES":
                        print("open scores...")
                        self.screen = "SCORES"
                    elif result == "INSTARUCTION":
                        print("open instaruction ...")
                        self.screen = "INSTARUCTION"
                    elif result == "QUIT":
                        self.run = False
                elif self.screen == "SCORES":
                    result = self.score.check_event(event)
                    if result == "MENU":
                        self.screen = "MENU"
                    elif result == "QUIT":
                        self.run = False
                elif self.screen == "INSTARUCTION":
                    result = self.instruction.check_event(event)
                    if result == "MENU":
                        self.screen = "MENU"
                    elif result == "QUIT":
                        self.run = False
            if self.screen == "MENU":
                self.menu.draw()
            elif self.screen == "SCORES":
                self.score.draw_scors()
            elif self.screen == "INSTARUCTION":
                self.instruction.display_ins()
        self.renderer.close()
