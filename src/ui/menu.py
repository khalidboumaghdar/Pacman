from src.ui.renderer import Renderer


class Menu:
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

        self.options = [
            "START",
            "SCORES",
            "INSTARUCTION",
            "QUIT"
        ]

        self.selected = 0

    def check_event(self, event: str) -> str | None:

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

    def __init__(self, renderer) -> None:

        self.renderer = renderer

        self.options = [
            "Resume the game",
            "Return to the main menu"
        ]

        self.selected = 0

    def check_event(self, event: str) -> str | None:

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

        width = 600
        height = 350

        x = 250
        y = 300

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
            x + 130,
            y + 50
        )

        for i, option in enumerate(self.options):

            text = option

            if i == self.selected:
                text = "> " + text

            self.renderer.draw_text(
                text,
                x + 70,
                y + 120 + i * 50
            )

        self.renderer.display()


class GameOver:
    def __int__(self):
        pass
