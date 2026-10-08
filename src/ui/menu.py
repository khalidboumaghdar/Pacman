class Menu:
    def __init__(self, renderer):
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