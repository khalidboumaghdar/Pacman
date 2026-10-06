from renderer import Renderer


class Score:
    def __init__(self, renderer: Renderer, heighscors: str) -> None:
        self.renderer: Renderer = renderer
        self.heighscors: str = heighscors

    def check_event(self, event: str):

        if event == "ENTER":
            return "MENU"

        if event == "QUIT":
            return "QUIT"

        return None

    def draw_scors(self) -> None:

        self.renderer.clear()

        self.renderer.draw_text(
            "SCORE-S",
            180,
            100
        )

        self.renderer.draw_text(
            "Press ENTER to go back",
            100,
            300
        )

        self.renderer.display()


class Insruction:
    def __init__(self, renderer: Renderer) -> None:
        self.renderer: Renderer = renderer

    def check_event(self, event: str) -> str | None:

        if event == "ENTER":
            return "MENU"

        if event == "QUIT":
            return "QUIT"

        return None

    def display_ins(self):
        self.renderer.clear()

        self.renderer.draw_text(
            "INSTRUCTION",
            150,
            50
        )

        self.renderer.draw_text(
            "ARROW KEYS: MOVE",
            80,
            150
        )

        self.renderer.draw_text(
            "EAT ALL PAC-DOTS",
            80,
            210
        )

        self.renderer.draw_text(
            "AVOID THE GHOSTS",
            80,
            270
        )

        self.renderer.draw_text(
            "ENTER: BACK TO MENU",
            80,
            350
        )

        self.renderer.display()
