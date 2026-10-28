from src.ui.renderer import Renderer
import pygame
import sys


class Menu:
    """This class use to menu principal"""
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

        self.options = [
            "START",
            "SCORES",
            "INSTRUCTION",
            "QUIT"
        ]

        self.selected = 0

    def check_event(self, event: str) -> str | None:
        """This method use to check events"""

        if event == "UP":
            self.selected -= 1

            if self.selected < 0:
                self.selected = len(self.options) - 1

        elif event == "DOWN":
            self.selected += 1

            if self.selected >= len(self.options):
                self.selected = 0

        elif event == "ENTER":
            return self.options[self.selected]

        elif event == "QUIT":
            return "QUIT"

        return None

    def draw(self) -> None:
        """This method use to draw text in menu"""
        self.renderer.clear()

        self.renderer.draw_text(
            "PAC-MAN",
            180,
            100
        )

        for i, option in enumerate(self.options):

            text = option

            if i == self.selected:
                text = "> " + text

            self.renderer.draw_text(
                text,
                180,
                200 + i * 60
            )

        self.renderer.display()


class Resume_game:
    """This class use to resum menu"""

    def __init__(self, renderer: Renderer) -> None:

        self.renderer = renderer

        self.options = [
            "Resume the game",
            "Return to the main menu"
        ]

        self.selected = 0

    def check_event(self, event: str) -> str | None:
        """This method use to check events"""
        if event == "UP":
            self.selected -= 1

            if self.selected < 0:
                self.selected = len(self.options) - 1

        elif event == "DOWN":
            self.selected += 1

            if self.selected >= len(self.options):
                self.selected = 0

        elif event == "ENTER":
            return self.options[self.selected]

        elif event == "QUIT":
            return "QUIT"

        return None

    def draw(self) -> None:
        """This method use to draw text in resum menu"""
        width = 2000
        height = 1500

        x = 0
        y = 0

        self.renderer.draw_body(
            x,
            y,
            width,
            height
        )

        self.renderer.draw_line(
            x,
            y,
            x + width,
            y,
            (255, 255, 255)
        )

        self.renderer.draw_line(
            x,
            y + height,
            x + width,
            y + height,
            (255, 255, 255)
        )

        self.renderer.draw_line(
            x,
            y,
            x,
            y + height,
            (255, 255, 255)
        )

        self.renderer.draw_line(
            x + width,
            y,
            x + width,
            y + height,
            (255, 255, 255)
        )

        self.renderer.draw_text(
            "PAUSE MENU",
            x + 50,
            y + 50
        )

        for i, option in enumerate(self.options):

            text = option

            if i == self.selected:
                text = "> " + text

            self.renderer.draw_text(
                text,
                x + 50,
                y + 120 + i * 50
            )

        self.renderer.display()


class GameOver:
    """This class use to GameOver menu"""
    def __init__(self, renderer: Renderer, score_fn: int) -> None:
        self.renderer: Renderer = renderer
        self.score_fn: int = score_fn

    def draw(self) -> None:
        """This method use to draw text in GameOver menu"""
        width = 2000
        height = 1500

        x = 0
        y = 0

        self.renderer.draw_body(
            x,
            y,
            width,
            height
        )

        self.renderer.draw_line(
            x,
            y,
            x + width,
            y,
            (255, 0, 255)
        )

        self.renderer.draw_line(
            x,
            y + height,
            x + width,
            y + height,
            (255, 255, 255)
        )

        self.renderer.draw_line(
            x,
            y,
            x,
            y + height,
            (255, 255, 255)
        )

        self.renderer.draw_line(
            x + width,
            y,
            x + width,
            y + height,
            (255, 255, 255)
        )
        self.renderer.draw_text(
            "GAME OVER",
            x + 50,
            y + 50
        )
        self.renderer.draw_text(
            "Final Scor : "+str(self.score_fn),
            x + 50,
            y + 100
        )

    def show(self) -> str:
        """This method use to enter name of user"""
        name = ""

        while True:
            self.draw()

            self.renderer.draw_text(
                "Enter your name: " + name,
                100,
                150
            )

            pygame.display.flip()

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if ev.type == pygame.KEYDOWN:

                    if ev.key == pygame.K_RETURN:
                        if name:
                            return name

                    elif ev.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    elif ev.unicode.isalnum() and len(name) < 10:
                        name += ev.unicode


class VicotryWindow:
    def __init__(self, renderer: Renderer, score_fn: int) -> None:
        self.renderer: Renderer = renderer
        self.score_fn: int = score_fn

    def draw(self) -> None:
        width = 2000
        height = 1500

        x = 0
        y = 0

        self.renderer.draw_body(
            x,
            y,
            width,
            height
        )

        self.renderer.draw_line(
            x,
            y,
            x + width,
            y,
            (255, 0, 255)
        )

        self.renderer.draw_line(
            x,
            y + height,
            x + width,
            y + height,
            (255, 255, 255)
        )

        self.renderer.draw_line(
            x,
            y,
            x,
            y + height,
            (255, 255, 255)
        )

        self.renderer.draw_line(
            x + width,
            y,
            x + width,
            y + height,
            (255, 255, 255)
        )
        self.renderer.draw_text(
            "YOU DID IT!",
            x + 50,
            y + 50
        )
        self.renderer.draw_text(
            "Amazing run! The maze is at peace thanks to you!",
            x + 50,
            y + 120
        )
        self.renderer.draw_text(
            "Final Scor : "+str(self.score_fn),
            x + 50,
            y + 290
        )

    def show(self) -> str:
        name = ""

        while True:
            self.draw()

            self.renderer.draw_text(
                "Enter your name: " + name,
                50,
                340
            )

            pygame.display.flip()

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if ev.type == pygame.KEYDOWN:

                    if ev.key == pygame.K_RETURN:
                        if name:
                            return name

                    elif ev.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    elif ev.unicode.isalnum() and len(name) < 10:
                        name += ev.unicode
