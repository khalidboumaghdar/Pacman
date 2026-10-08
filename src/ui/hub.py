from src.ui.renderer import Renderer
from src.ui.menu import Menu
from src.ui.screens import Score, Insruction
from src.core.runGame import RunGame
import sys


class Hub:
    def __init__(self):
        self.renderer = Renderer(2000, 1500, "Pac-Man")
        self.menu = Menu(self.renderer)
        self.score = Score(self.renderer, "heighscors.json")
        self.instruction = Insruction(self.renderer)
        self.screen = "MENU"
        self.run = True
        self.runGame = None


    def runMenu(self):
        while self.run:
            events = self.renderer.event()
            for event in events:
                if self.screen == "MENU":
                    result = self.menu.check_event(event)
                    if result == "START":
                        print("start game...")
                        self.runGame = RunGame()
                        self.runGame.runGame()
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